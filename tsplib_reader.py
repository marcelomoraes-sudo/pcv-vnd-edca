import math
import os

def ler_instancia_tsplib(caminho_arquivo):
    """
    Lê uma instância no formato TSPLIB e retorna o número de cidades 
    e a matriz de custos com distâncias euclidianas arredondadas (EUC_2D).
    """
    if not os.path.exists(caminho_arquivo):
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho_arquivo}")
        
    coordenadas = {}
    ler_coordenadas = False
    dimensao = 0
    
    with open(caminho_arquivo, 'r') as f:
        for linha in f:
            linha = linha.strip()
            if linha.startswith("DIMENSION"):
                dimensao = int(linha.split(":")[-1].strip())
            elif linha.startswith("NODE_COORD_SECTION"):
                ler_coordenadas = True
                continue
            elif linha == "EOF" or not linha:
                break
                
            if ler_coordenadas:
                partes = linha.split()
                if len(partes) >= 3:
                    idx = int(partes[0]) - 1 # Indexação baseada em 0
                    x = float(partes[1])
                    y = float(partes[2])
                    coordenadas[idx] = (x, y)
                    
    # Construção da matriz de custos n x n
    matriz_custos = [[0.0 for _ in range(dimensao)] for _ in range(dimensao)]
    for i in range(dimensao):
        for j in range(dimensao):
            if i != j:
                x1, y1 = coordenadas[i]
                x2, y2 = coordenadas[j]
                # Distância Euclidiana Padrão TSPLIB (Arredondada para o inteiro mais próximo)
                xd = x1 - x2
                yd = y1 - y2
                dij = math.sqrt(xd*xd + yd*yd)
                matriz_custos[i][j] = int(dij + 0.5)
            else:
                matriz_custos[i][j] = float('inf') # Evita laços de uma cidade para ela mesma
                
    return dimensao, matriz_custos
