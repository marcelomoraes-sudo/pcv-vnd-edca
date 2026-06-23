import time
from tsplib_reader import ler_instancia_tsplib
from algoritmo_vnd import executar_vnd

def rodar_experimentos():
    # Instâncias selecionadas no seu relatório
    instancias = [
        {"nome": "berlin52", "arquivo": "data/berlin52.tsp"},
        {"nome": "st70", "arquivo": "data/st70.tsp"},
        {"nome": "eil101", "arquivo": "data/eil101.tsp"},
        {"nome": "ch150", "arquivo": "data/ch150.tsp"},
        {"nome": "a280", "arquivo": "data/a280.tsp"}#,
#        {"nome": "pr1002", "arquivo": "data/pr1002.tsp"}
    ]
    
    # Número de execuções para extrair uma média estatística confiável de tempo
    num_execucoes = 5
    
    print("=" * 75)
    print(f"{'RESULTADOS COMPUTACIONAIS - META-HEURÍSTICA VND':^75}")
    print("=" * 75)
    print(f"{'Instância':<15} | {'Cidades':<8} | {'Melhor Custo':<15} | {'Tempo Médio (s)':<15}")
    print("-" * 75)
    
    for inst in instancias:
        try:
            # Carrega os dados da instância
            n, matriz_custos = ler_instancia_tsplib(inst["arquivo"])
            
            tempos = []
            melhor_custo = float('inf')
            
            # Loop de medição de desempenho
            for _ in range(num_execucoes):
                inicio_tempo = time.perf_counter()
                _, custo_obtido = executar_vnd(n, matriz_custos)
                fim_tempo = time.perf_counter()
                
                tempos.append(fim_tempo - inicio_tempo)
                if custo_obtido < melhor_custo:
                    melhor_custo = custo_obtido
                    
            tempo_medio = sum(tempos) / len(tempos)
            
            print(f"{inst['nome']:<15} | {n:<8} | {melhor_custo:<15} | {tempo_medio:.5f}s")
            
        except FileNotFoundError:
            print(f"{inst['nome']:<15} | ERR      | Arquivo .tsp ausente na pasta 'data/'")
            
    print("=" * 75)

if __name__ == "__main__":
    rodar_experimentos()
