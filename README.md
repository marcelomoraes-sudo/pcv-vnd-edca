# Problema do Caixeiro Viajante (PCV) com Meta-heurística VND

Este repositório contém a implementação prática da **Atividade A2** para a disciplina de **Estrutura de Dados e Complexidade de Algoritmos** do programa de Pós-Graduação (Mestrado) em Informática da Universidade Federal da Paraíba (UFPB).

O objetivo deste projeto é resolver o Problema do Caixeiro Viajante (PCV) utilizando uma abordagem híbrida: uma heurística construtiva de inicialização rápida seguida pelo refinamento através da meta-heurística **Variable Neighborhood Descent (VND)**.

## 🚀 Estrutura do Algoritmo

1. **Representação da Solução:** Vetor de inteiros de tamanho $n$, onde cada elemento representa o índice de uma cidade visitada, assumindo implicitamente o retorno da última cidade para a primeira.
2. **Heurística de Construção:** Algoritmo do **Vizinho Mais Próximo**, iniciando estrategicamente na cidade `0` para determinar um ponto de partida viável.
3. **Estruturas de Vizinhança:**
   - **$N_1$: *Swap*** (Troca de vértices): Avalia a troca de posição entre cada par de cidades. Opera sob a estratégia de Melhor Melhora (*Best Improvement*).
   - **$N_2$: *2-Opt*** (Troca de arestas): Remove duas arestas não adjacentes e reconecta a rota invertendo o segmento intermediário, eliminando cruzamentos geográficos. Opera sob Melhor Melhora (*Best Improvement*).

## 📁 Estrutura de Diretórios

```text
pcv_vnd/
├── data/                  # Instâncias oficiais em formato .tsp da TSPLIB
├── tsplib_reader.py       # Módulo de leitura e cálculo de matriz de distâncias (EUC_2D)
├── algoritmo_vnd.py       # Núcleo do algoritmo (Construtivo, Vizinhanças e laço VND)
├── main.py                # Script de execução, medição de tempo e consolidação dos testes
└── README.md              # Documentação do repositório

```

## 🛠️ Como Executar

### Pré-requisitos

* Python 3.8 ou superior instalado.
* Ferramenta de terminal (`wget` ou `curl`) para descarregar as instâncias originais.

### Passo 1: Clonar o repositório e aceder à pasta

```bash
git clone [https://github.com/marcelomoraes-sudo/pcv-vnd-edca.git](https://github.com/marcelomoraes-sudo/pcv-vnd-edca.git)
cd pcv-vnd-edca

```

### Passo 2: Descarregar as instâncias da TSPLIB

Obs.: O repositório já conta com seis instancias descarregadas.

Execute os comandos abaixo para criar o diretório de dados e buscar as instâncias do repositório oficial da Universidade de Heidelberg:

```bash
mkdir -p data
cd data
curl -L -O [http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/tsp/ulysses26.tsp](http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/tsp/ulysses26.tsp)
curl -L -O [http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/tsp/att48.tsp](http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/tsp/att48.tsp)
curl -L -O [http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/tsp/berlin52.tsp](http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/tsp/berlin52.tsp)
curl -L -O [http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/tsp/ch150.tsp](http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/tsp/ch150.tsp)
cd ..

```

### Passo 3: Rodar os experimentos computacionais


* Rodando o teste em todos os arquivos listados no código do `main.py` e apresentará uma tabela com o resumo de cada arquivo.

```bash
python main.py

```

* Rodando para apenas um arquivo específico, além de apresentar uma tabela com o resumo do arquivo, serão exibidos os momentos quando houve mudança entre 2-opt e swap.

```bash
python main.py data/berlin52.tsp

```

## 📊 Resultados Computacionais Obtidos


```text

moraes@vm-marcelo:~/vnd$ python3 main.py

>> BATERIA DE TESTES AUTOMÁTICA: Processando silenciosamente...

 -> Calculando métricas para berlin52...
 -> Calculando métricas para st70...
 -> Calculando métricas para eil101...
 -> Calculando métricas para ch150...
 -> Calculando métricas para a280...

==========================================================================================
                    TABELA CONSOLIDADA DE RESULTADOS - METRICAS FINAIS
==========================================================================================
Instância       | Cidades  | Custo Final   | Uso Swap   | Uso 2-Opt  | Tempo (s)
------------------------------------------------------------------------------------------
berlin52        | 52       | 7749          | 18         | 5          | 0.04636s
st70            | 70       | 701           | 21         | 5          | 0.11006s
eil101          | 101      | 648           | 25         | 8          | 0.41230s
ch150           | 150      | 7009          | 22         | 10         | 1.41409s
a280            | 280      | 2817          | 34         | 18         | 15.39067s
==========================================================================================
moraes@vm-marcelo:~/vnd$

```
ou


```text

moraes@vm-marcelo:~/vnd$ python3 main.py data/berlin52.tsp

>> MODO ESPECÍFICO DETALHADO: data/berlin52.tsp

=====================================================================================
 PROCESSANDO INSTÂNCIA: BERLIN52
=====================================================================================
   [Fase Construtiva] Solução Inicial - Custo: 8980
   --> Explorando Vizinhança N1 (SWAP)... [MELHOROU: 8980 -> 8901]
   --> Explorando Vizinhança N1 (SWAP)... [MELHOROU: 8901 -> 8840]
   --> Explorando Vizinhança N1 (SWAP)... [MELHOROU: 8840 -> 8780]
   --> Explorando Vizinhança N1 (SWAP)... [MELHOROU: 8780 -> 8765]
   --> Explorando Vizinhança N1 (SWAP)... [MELHOROU: 8765 -> 8751]
   --> Explorando Vizinhança N1 (SWAP)... [MELHOROU: 8751 -> 8619]
   --> Explorando Vizinhança N1 (SWAP)... [MELHOROU: 8619 -> 8614]
   --> Explorando Vizinhança N1 (SWAP)... [Sem melhora local]
   --> Explorando Vizinhança N2 (2-OPT)... [MELHOROU: 8614 -> 8357]
   --> Explorando Vizinhança N1 (SWAP)... [Sem melhora local]
   --> Explorando Vizinhança N2 (2-OPT)... [MELHOROU: 8357 -> 8090]
   --> Explorando Vizinhança N1 (SWAP)... [MELHOROU: 8090 -> 8078]
   --> Explorando Vizinhança N1 (SWAP)... [MELHOROU: 8078 -> 8011]
   --> Explorando Vizinhança N1 (SWAP)... [Sem melhora local]
   --> Explorando Vizinhança N2 (2-OPT)... [MELHOROU: 8011 -> 7957]
   --> Explorando Vizinhança N1 (SWAP)... [MELHOROU: 7957 -> 7934]
   --> Explorando Vizinhança N1 (SWAP)... [MELHOROU: 7934 -> 7917]
   --> Explorando Vizinhança N1 (SWAP)... [MELHOROU: 7917 -> 7903]
   --> Explorando Vizinhança N1 (SWAP)... [Sem melhora local]
   --> Explorando Vizinhança N2 (2-OPT)... [MELHOROU: 7903 -> 7814]
   --> Explorando Vizinhança N1 (SWAP)... [MELHOROU: 7814 -> 7749]
   --> Explorando Vizinhança N1 (SWAP)... [Sem melhora local]
   --> Explorando Vizinhança N2 (2-OPT)... [Sem melhora local]
   [VND Concluído] Custo Final Otimizado: 7749


==========================================================================================
                    TABELA CONSOLIDADA DE RESULTADOS - METRICAS FINAIS
==========================================================================================
Instância       | Cidades  | Custo Final   | Uso Swap   | Uso 2-Opt  | Tempo (s)
------------------------------------------------------------------------------------------
berlin52        | 52       | 7749          | 18         | 5          | 0.05167s
==========================================================================================
moraes@vm-marcelo:~/vnd$

```


*Nota: Os valores de tempo e custo acima podem variar ligeiramente dependendo do ambiente de hardware onde o script for executado.*

## 👤 Autor

* **Marcelo da Silva Moraes** - Mestrado em Informática (UFPB)
* Matrícula: 20261001638
* E-mail: marcelo.moraes@sti.ufpb.br

