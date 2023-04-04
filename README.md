# Estrutura de Dados e Algoritmos

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/ovalves/algorithms/blob/master/LICENSE)

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
* **Architecture**
  * `A` [Exponential Backoff and jitter](src/architecture/exponential-backoff-and-jitter)
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
  * `B` [Palindrome Number](src/problems/palindrome-number)
  * `A` [Gene Compression](src/problems/gene-compression)
  * `B` [Leibniz π](src/problems/calculating-pi)
  * `B` [One time pad](src/problems/one-time-pad)
  * `B` [Roman to Integer](src/problems/roman-to-integer)
  * `B` [Sort Colors](src/problems/sort-colors)
  * `B` [Sort Characters By Frequency](src/problems/sort-characters-by-frequency)
  * `B` [Reverse Words In a String](src/problems/reverse-words-in-a-string)
  * `B` [Min Stack](src/problems/min-stack)
  * `B` [Transpose Matrix](src/problems/transpose-matrix)
  * `B` [Two Sum](src/problems/two-sum)
  * `A` [Best Time to Buy and Sell Stock II](src/problems/best-time-to-buy-sell-stock)
  * `A` [Combination Sum IV](src/problems/combination-sum-iv)
  * `B` [Fibonacci](src/problems/fibonacci/solution.go)

## Técnicas usadas

### Recursão
A recursão, em particular, está no coração não só de vários algoritmos, mas até mesmo em linguagens de programação completas.

Em algumas linguagens de programação funcional, como Scheme e Haskell, a recursão substitui os laços usados nas linguagens imperativas. Contudo, vale a pena lembrar que tudo que pode ser feito com uma técnica recursiva também pode sê-lo com uma técnica iterativa.


### Memoização
A memoização tem sido aplicada com sucesso para agilizar o trabalho dos parsers (programas que interpretam linguagens). É útil para todos os problemas nos quais o resultado de um cálculo recente será provavelmente solicitado de novo.

Outra aplicação da memoização está nos runtimes de linguagens. Alguns runtimes de linguagens (versões de Prolog, por exemplo) armazenam os resultados das chamadas de funções automaticamente (automemoização), de modo que a função não precisará executar da próxima vez que a mesma chamada for feita.

### Compactação
A compactação tem feito com que um mundo conectado pela internet com limitações de largura de banda seja mais tolerável.

A técnica de cadeia de bits pode ser usada para tipos de dados simples do mundo real que tenham um número limitado de valores possíveis, para os quais mesmo um byte poderia ser um exagero.

A maioria dos algoritmos de compactação, porém, atua encontrando padrões ou estruturas em um conjunto de dados, os quais permitem que informações repetidas sejam eliminadas.


### Notação Big O

* Usado para realizar a comparação objetiva entre algoritimos
* O quanto a "complexidade"do algoritmo aumenta de acordo com as entradas

Ordem de crescimento dos algoritmos especificados em notação Big O

![Notação Big-O](assets/big-o-graph.png)

Fonte: [Notação Big-O dicas](http://bigocheatsheet.com/).

### Notações Big O mais usadas e comparação de desempenho em relação aos diferentes tamanhos dos dados de entrada.

| Notação Big-O         | Nome         | Calc. 10 itens | Calc. 100 itens | Calc. 1000 itens |
| --------------------- | ------------ | -------------- | --------------- | -----------------|
| **O(1)**              | Constant     | 1              | 1               | 1                |
| **O(log n)**          | Logarithmic  | 3              | 6               | 9                |
| **O(n)**              | Linear       | 10             | 100             | 1000             |
| **O(n * log(n))**     | Linearithmic | 30             | 600             | 9000             |
| **O(n<sup>2</sup>)**  | Quadratic    | 100            | 10000           | 1000000          |
| **O(2<sup>n</sup>)**  | Exponential  | 1024           | 1.26e+29        | 1.07e+301        |
| **O(n!)**             | Factorial    | 3628800        | 9.3e+157        | 4.02e+2567       |

### Complexidade de operações em estrutura de dados

| estrutura de dados      | Acesso    | Busca     | Inserção  | Deleção   |
| ----------------------- | --------- | --------- | --------- | --------- |
| **Array**               | O(1)      | O(n)      | O(n)      | O(n)      |
| **Stack**               | O(n)      | O(n)      | O(1)      | O(1)      |
| **Queue**               | O(n)      | O(n)      | O(1)      | O(1)      |
| **Linked List**         | O(n)      | O(n)      | O(1)      | O(1)      |
| **Hash Table**          | -         | O(n)      | O(n)      | O(n)      |
| **Binary Search Tree**  | O(n)      | O(n)      | O(n)      | O(n)      |
| **B-Tree**              | O(log(n)) | O(log(n)) | O(log(n)) | O(log(n)) |
| **Red-Black Tree**      | O(log(n)) | O(log(n)) | O(log(n)) | O(log(n)) |
| **AVL Tree**            | O(log(n)) | O(log(n)) | O(log(n)) | O(log(n)) |
| **Bloom Filter**        | -         | O(1)      | O(1)      | -         |

### Complexidade dos algoritmos para Ordenação de Array

| Nome                  | Melhor Cenário   | Cenário OK                      | Pior Cenário              | Mémoria   | Estável |
| --------------------- | ---------------- | ------------------------------- | ------------------------  | --------- | ------- |
| **Bubble sort**       | O(n)             | O(n<sup>2</sup>)                | O(n<sup>2</sup>)          | 1         | Sim     |
| **Insertion sort**    | O(n)             | O(n<sup>2</sup>)                | O(n<sup>2</sup>)          | 1         | Sim     |
| **Selection sort**    | O(n<sup>2</sup>) | O(n<sup>2</sup>)                | O(n<sup>2</sup>)          | 1         | Não     |
| **Heap sort**         | O(n log(n))      | O(n log(n))                     | O(n log(n))               | 1         | Não     |
| **Merge sort**        | O(n log(n))      | O(n log(n))                     | O(n log(n))               | n         | Sim     |
| **Quick sort**        | O(n log(n))      | O(n log(n))                     | O(n<sup>2</sup>)          | log(n)    | Não     |
| **Shell sort**        | O(n log(n))      | depende da sequência de lacunas | O(n (log(n))<sup>2</sup>) | 1         | Não     |
| **Counting sort**     | O(n + r)         | O(n + r)                        | O(n + r)                  | n + r     | Sim     |
| **Radix sort**        | O(n * k)         | O(n * k)                        | O(n * k)                  | n + k     | Sim     |

### Referências

- [Estruturas de dados e algoritmos no YouTube](https://www.youtube.com/playlist?list=PLLXdhg_r2hKA7DPDsunoDZ-Z769jWn4R8)
- [Estrutura de Dados e Algoritmos em JavaScript](https://github.com/trekhleb/javascript-algorithms/blob/master/README.md)