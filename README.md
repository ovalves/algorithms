# Estrutura de Dados e Algoritmos

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/ovalves/algorithms/blob/master/LICENSE)
[![PR's Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat)](http://makeapullrequest.com)

Este repositório contém algoritmos e estruturas de dados populares.

Cada algoritmo e estrutura de dado possui seu próprio README
com explicações relacionadas e links para leitura adicional

## Estruturas de dados

Uma estrutura de dados é uma maneira particular de organizar e armazenar dados em um computador para que ele possa
ser acessado e modificado de forma eficiente. Mais precisamente, uma estrutura de dados é uma coleção de dados
valores, as relações entre eles e as funções ou operações que podem ser aplicadas aos dados.

`B` - Iniciante, `A` - Avançado

* `B` [Lista Encadeada (Linked List)](src/data-structures/linked-list/singly)
* `B` [Lista Duplamente Ligada (Doubly Linked List)](src/data-structures/linked-list/doubly)
* `B` [Fila (Queue)](src/data-structures/queue)

## Algoritmos

Um algoritmo é uma especificação inequívoca de como resolver uma classe de problemas. Isto é
um conjunto de regras que define precisamente uma sequência de operações.

`B` - Iniciante, `A` - Avançado

### Algoritmos por Tópico
* **Inteligência Artificil e Machine Learning**
  * `A` [Sistemas de recomendação](src/machine-learning/recommender)
  * `B` [Rede Neural - Perceptron de uma camada](src/artificial-intelligence/neural-network/single-layer)
  * Algoritmos de Otimização
    * `A` [Algoritmos genéticos](src/artificial-intelligence/genetic-algorithms)

* **Buscas**
  * `B` [Binary Search](src/algorithms/search/binary-search)

* **Ordenação**
  * `B` [Bubble Sort](src/algorithms/sorting/bubble-sort)
  * `B` [Selection Sort](src/algorithms/sorting/selection-sort)
  * `B` [Insertion Sort](src/algorithms/sorting/insertion-sort)
  * `B` [Shell Sort](src/algorithms/sorting/shell-sort)
  * `B` [Merge Sort](src/algorithms/sorting/merge-sort)
  * `B` [Quicksort](src/algorithms/sorting/quick-sort)

* **Sem Categoria**
  * `B` [Soma Recursiva](src/algorithms/uncategorized/recursive)

* **Problemas**
  * `A` [Median of Two Sorted Arrays](src/problems/median-of-two-sorted-arrays)
  * `B` [Reverse Integer](src/problems/reverse-integer)

### Referências

[Estruturas de dados e algoritmos no YouTube](https://www.youtube.com/playlist?list=PLLXdhg_r2hKA7DPDsunoDZ-Z769jWn4R8)

[Estrutura de Dados e Algoritmos em JavaScript](https://github.com/trekhleb/javascript-algorithms/blob/master/README.md)

### Notação Big O

* Usado para realizar a comparação objetiva entre algoritimos
* O quanto a "complexidade"do algoritmo aumenta de acordo com as entradas

Ordem de crescimento dos algoritmos especificados em notação Big O

![Notação Big-O](assets/big-o-graph.png)

Fonte: [Notação Big-O dicas](http://bigocheatsheet.com/).

Abaixo está a lista de algumas das notações Big O mais usadas e suas comparações de desempenho em relação aos diferentes tamanhos dos dados de entrada.

| Notação Big-O  | Cálculos para 10 elementos   | Cálculos para 100 elementos   | Cálculos para 1000 elementos    |
| -------------- | ---------------------------- | ----------------------------- | ------------------------------- |
| **O(1)**       | 1                            | 1                             | 1                               |
| **O(log N)**   | 3                            | 6                             | 9                               |
| **O(N)**       | 10                           | 100                           | 1000                            |
| **O(N log N)** | 30                           | 600                           | 9000                            |
| **O(N^2)**     | 100                          | 10000                         | 1000000                         |
| **O(2^N)**     | 1024                         | 1.26e+29                      | 1.07e+301                       |
| **O(N!)**      | 3628800                      | 9.3e+157                      | 4.02e+2567                      |

### Complexidade de operações de estrutura de dados

| estrutura de dados      | Acesso    | Busca     | Inserção  | Eliminação | comentários |
| ----------------------- | :-------: | :-------: | :-------: | :-------:  | :--------   |
| **Array**               | 1         | n         | n         | n          |             |
| **Stack**               | n         | n         | 1         | 1          |             |
| **Queue**               | n         | n         | 1         | 1          |             |
| **Linked List**         | n         | n         | 1         | 1          |             |
| **Hash Table**          | -         | n         | n         | n          | Em caso de uma função hash perfeita, os custos seriam O (1) |
| **Binary Search Tree**  | n         | n         | n         | n          | No caso de custos de árvore equilibrados seria O (log (n))
| **B-Tree**              | log(n)    | log(n)    | log(n)    | log(n)     |             |
| **Red-Black Tree**      | log(n)    | log(n)    | log(n)    | log(n)     |             |
| **AVL Tree**            | log(n)    | log(n)    | log(n)    | log(n)     |             |
| **Bloom Filter**        | -         | 1         | 1         | -          | Falsos positivos são possíveis durante a pesquisa |

### Array Sorting Algorithms Complexity

| Nome                  | Melhor          | Média               | Pior                | Mémoria   | Estável   | comentários |
| --------------------- | :-------------: | :-----------------: | :-----------------: | :-------: | :-------: | :--------   |
| **Bubble sort**       | n               | n<sup>2</sup>       | n<sup>2</sup>       | 1         | Sim       |             |
| **Insertion sort**    | n               | n<sup>2</sup>       | n<sup>2</sup>       | 1         | Sim       |             |
| **Selection sort**    | n<sup>2</sup>   | n<sup>2</sup>       | n<sup>2</sup>       | 1         | Não       |             |
| **Heap sort**         | n&nbsp;log(n)   | n&nbsp;log(n)       | n&nbsp;log(n)       | 1         | Não       |             |
| **Merge sort**        | n&nbsp;log(n)   | n&nbsp;log(n)       | n&nbsp;log(n)       | n         | Sim       |             |
| **Quick sort**        | n&nbsp;log(n)   | n&nbsp;log(n)       | n<sup>2</sup>       | log(n)    | Não       | O Quicksort geralmente é feito no local com o espaço de pilha O  O(log(n)) stack space |
| **Shell sort**        | n&nbsp;log(n)   | depende da sequência de lacunas | n&nbsp;(log(n))<sup>2</sup>     | 1      | Não    |                   |
| **Counting sort**     | n + r           | n + r               | n + r               | n + r     | Sim       | r - maior número na matriz          |
| **Radix sort**        | n * k           | n * k               | n * k               | n + k     | Sim       | k - comprimento da chave mais longa |
