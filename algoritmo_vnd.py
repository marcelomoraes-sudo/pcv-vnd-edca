import copy

def calcular_custo_total(rota, matriz_custos):
    """
    Calcula o custo total da rota, considerando o retorno à origem.
    """
    n = len(rota)
    custo = 0
    for i in range(n - 1):
        custo += matriz_custos[rota[i]][rota[i+1]]
    custo += matriz_custos[rota[-1]][rota[0]] # Retorno à cidade inicial
    return custo

def heuristica_vizinho_mais_proximo(n, matriz_custos, cidade_inicial=0):
    """
    Heurística Construtiva: Constrói uma solução inicial viável 
    escolhendo sempre a cidade mais próxima ainda não visitada.
    """
    visitados = [False] * n
    rota = [cidade_inicial]
    visitados[cidade_inicial] = True
    
    cidade_atual = cidade_inicial
    for _ in range(n - 1):
        proxima_cidade = -1
        menor_distancia = float('inf')
        
        # Procura pelo vizinho mais próximo não visitado
        for j in range(n):
            if not visitados[j] and matriz_custos[cidade_atual][j] < menor_distancia:
                menor_distancia = matriz_custos[cidade_atual][j]
                proxima_cidade = j
                
        rota.append(proxima_cidade)
        visitados[proxima_cidade] = True
        cidade_atual = proxima_cidade
        
    return rota

def melhor_vizinho_swap(rota_atual, custo_atual, matriz_custos):
    """
    Vizinhança N1 - Swap (Best Improvement):
    Testa todas as trocas de pares de cidades. Retorna a melhor encontrada.
    """
    n = len(rota_atual)
    melhor_rota = rota_atual
    melhor_custo = custo_atual
    
    for i in range(n - 1):
        for j in range(i + 1, n):
            # Cria o vizinho trocando as posições i e j
            nova_rota = list(rota_atual)
            nova_rota[i], nova_rota[j] = nova_rota[j], nova_rota[i]
            
            novo_custo = calcular_custo_total(nova_rota, matriz_custos)
            
            if novo_custo < melhor_custo:
                melhor_custo = novo_custo
                melhor_rota = nova_rota
                
    return melhor_rota, melhor_custo

def melhor_vizinho_2opt(rota_atual, custo_atual, matriz_custos):
    """
    Vizinhança N2 - 2-Opt (Best Improvement):
    Remove duas arestas e inverte o segmento intermediário da rota.
    """
    n = len(rota_atual)
    melhor_rota = rota_atual
    melhor_custo = custo_atual
    
    for i in range(1, n - 2):
        for j in range(i + 1, n):
            if j - i == 1: continue # Evita arestas adjacentes comuns
            
            # Aplica o movimento 2-opt: inverte o trecho de i até j
            nova_rota = rota_atual[:]
            nova_rota[i:j] = reversed(nova_rota[i:j])
            
            novo_custo = calcular_custo_total(nova_rota, matriz_custos)
            
            if novo_custo < melhor_custo:
                melhor_custo = novo_custo
                melhor_rota = nova_rota
                
    return melhor_rota, melhor_custo

def executar_vnd(n, matriz_custos):
    """
    Estrutura principal da Meta-heurística Variable Neighborhood Descent (VND).
    Altera sistematicamente entre as vizinhanças N1 e N2 ao encontrar ótimos locais.
    """
    # 1. Fase de Construção
    rota = heuristica_vizinho_mais_proximo(n, matriz_custos, cidade_inicial=0)
    custo = calcular_custo_total(rota, matriz_custos)
    
    k = 1
    k_max = 2 # N1 = Swap, N2 = 2-Opt
    
    while k <= k_max:
        if k == 1:
            nova_rota, novo_custo = melhor_vizinho_swap(rota, custo, matriz_custos)
        elif k == 2:
            nova_rota, novo_custo = melhor_vizinho_2opt(rota, custo, matriz_custos)
            
        # Se houver melhora estrita, atualiza a solução e retorna à vizinhança N1
        if novo_custo < custo:
            rota = nova_rota
            custo = novo_custo
            k = 1 
        else:
            k += 1 # Se não houver melhora, avança para a próxima estrutura de vizinhança
            
    return rota, custo
