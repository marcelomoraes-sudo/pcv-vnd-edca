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

```bash
python main.py

```

## 📊 Resultados Computacionais Obtidos

O script executa cada instância de forma repetida (5 vezes) para extrair a média exata do tempo computacional em segundos utilizando o marcador de alta precisão `time.perf_counter()`.

```text

moraes@vm-marcelo:~/vnd$ python3 main.py
===========================================================================
              RESULTADOS COMPUTACIONAIS - META-HEURÍSTICA VND
===========================================================================
Instância       | Cidades  | Melhor Custo    | Tempo Médio (s)
---------------------------------------------------------------------------
berlin52        | 52       | 7749            | 0.04472s
st70            | 70       | 701             | 0.10989s
eil101          | 101      | 648             | 0.41581s
ch150           | 150      | 7009            | 1.42008s
a280            | 280      | 2817            | 15.06222s
===========================================================================

```

*Nota: Os valores de tempo e custo acima podem variar ligeiramente dependendo do ambiente de hardware onde o script for executado.*

## 👤 Autor

* **Marcelo da Silva Moraes** - Mestrado em Informática (UFPB)
* Matrícula: 20261001638
* E-mail: marcelo.moraes@sti.ufpb.br

