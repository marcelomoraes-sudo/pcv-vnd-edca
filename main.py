import time
import sys
import os
from tsplib_reader import ler_instancia_tsplib
from algoritmo_vnd import executar_vnd

def rodar_experimentos():
    instancias_padrao = [
        {"nome": "berlin52", "arquivo": "data/berlin52.tsp"},
        {"nome": "st70", "arquivo": "data/st70.tsp"},
        {"nome": "eil101", "arquivo": "data/eil101.tsp"},
        {"nome": "ch150", "arquivo": "data/ch150.tsp"},
        {"nome": "a280", "arquivo": "data/a280.tsp"}#,
        #### O arquivo abaixo demora muito, devido a quantidade de cidades. 
        #### Por conta disso, retirei da lista de testes.
#        {"nome": "pr1002", "arquivo": "data/pr1002.tsp"}
    ]
    
    if len(sys.argv) > 1:
        caminho_customizado = sys.argv[1]
        nome_instancia = os.path.basename(caminho_customizado).replace(".tsp", "")
        instancias_para_rodar = [{"nome": nome_instancia, "arquivo": caminho_customizado}]
        modo_detalhado = True
        print(f"\n>> MODO ESPECÍFICO DETALHADO: {caminho_customizado}\n")
    else:
        instancias_para_rodar = instancias_padrao
        modo_detalhado = False
        print("\n>> BATERIA DE TESTES AUTOMÁTICA: Processando silenciosamente...\n")

    resumo_resultados = []
    
    for inst in instancias_para_rodar:
        try:
            if modo_detalhado:
                print("=" * 85)
                print(f" PROCESSANDO INSTÂNCIA: {inst['nome'].upper()}")
                print("=" * 85)
            else:
                print(f" -> Calculando métricas para {inst['nome']}...")
                
            n, matriz_custos = ler_instancia_tsplib(inst["arquivo"])
            
            inicio_tempo = time.perf_counter()
            # Captura o terceiro retorno contendo os contadores
            _, custo_obtido, qtd_usos = executar_vnd(n, matriz_custos, verbose=modo_detalhado)
            fim_tempo = time.perf_counter()
            
            tempo_execucao = fim_tempo - inicio_tempo
            
            resumo_resultados.append({
                "nome": inst['nome'],
                "cidades": n,
                "custo": custo_obtido,
                "tempo": tempo_execucao,
                "qtd_swap": qtd_usos["swap"],
                "qtd_2opt": qtd_usos["two_opt"]
            })
            
        except FileNotFoundError:
            print(f"[ERRO] Arquivo ausente em: '{inst['arquivo']}'")
            resumo_resultados.append({
                "nome": inst['nome'], "cidades": "ERR", "custo": "N/A", "tempo": 0.0, "qtd_swap": 0, "qtd_2opt": 0
            })
            
    # TABELA CONSOLIDADA FINAL EXPANDIDA
    print("\n" + "=" * 90)
    print(f"{'TABELA CONSOLIDADA DE RESULTADOS - METRICAS FINAIS':^90}")
    print("=" * 90)
    print(f"{'Instância':<15} | {'Cidades':<8} | {'Custo Final':<13} | {'Uso Swap':<10} | {'Uso 2-Opt':<10} | {'Tempo (s)':<12}")
    print("-" * 90)
    for res in resumo_resultados:
        if isinstance(res['tempo'], float) and res['tempo'] > 0:
            print(f"{res['nome']:<15} | {res['cidades']:<8} | {res['custo']:<13} | {res['qtd_swap']:<10} | {res['qtd_2opt']:<10} | {res['tempo']:.5f}s")
        else:
            print(f"{res['nome']:<15} | {res['cidades']:<8} | {res['custo']:<13} | --         | --         | --")
    print("=" * 90)

if __name__ == "__main__":
    rodar_experimentos()

