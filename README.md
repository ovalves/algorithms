# Estrutura de Dados e Algoritmos

[![MIT License](https://img.shields.io/github/license/ovalves/algorithms)](https://github.com/ovalves/algorithms/blob/main/LICENSE)

Este repositório contém algoritmos e estruturas de dados populares.

Cada algoritmo e estrutura de dado possui seu próprio README
com explicações relacionadas e links para leitura adicional

## Estruturas de dados

Uma estrutura de dados é uma maneira particular de organizar e armazenar dados em um computador para que ele possa
ser acessado e modificado de forma eficiente. Mais precisamente, uma estrutura de dados é uma coleção de dados
valores, as relações entre eles e as funções ou operações que podem ser aplicadas aos dados.

* [Arrays](src/data-structures/array)
* [Hash Table](src/data-structures/hashtables)
* [Linked List](src/data-structures/lists/linked-list/singly)
* [Doubly Linked List](src/data-structures/lists/linked-list/doubly)
* [Stacks & Queue](src/data-structures/stacks-queue)

## Algoritmos

Um algoritmo é uma especificação inequívoca de como resolver uma classe de problemas. Isto é
um conjunto de regras que define precisamente uma sequência de operações.

### Algoritmos por Tópico
* **Architecture**
  * [Exponential Backoff and jitter](src/architecture/exponential-backoff-and-jitter)
* **Inteligência Artificil e Machine Learning**
  * [Sistemas de recomendação](src/ml-ia/ml/recommender)
  * [Rede Neural - Perceptron de uma camada](src/ml-ia/ia/neural-network/single-layer)
  * Algoritmos de Otimização
    * [Algoritmos genéticos](src/ml-ia/ia/genetic-algorithms)

* **Buscas**
  * [Binary Search](src/algorithms/search/binary-search)

* **Ordenação**
  * [Bubble Sort](src/algorithms/sorting/bubble-sort)
  * [Selection Sort](src/algorithms/sorting/selection-sort)
  * [Insertion Sort](src/algorithms/sorting/insertion-sort)
  * [Shell Sort](src/algorithms/sorting/shell-sort)
  * [Merge Sort](src/algorithms/sorting/merge-sort)
  * [Quicksort](src/algorithms/sorting/quick-sort)

* **Problemas**
  * [Median of Two Sorted Arrays](src/problems/median-of-two-sorted-arrays)
  * [Reverse Integer](src/problems/reverse-integer)
  * [Palindrome Number](src/problems/palindrome-number)
  * [Soma Recursiva](src/problems/recursive-sum)
  * [Gene Compression](src/problems/gene-compression)
  * [Leibniz π](src/problems/calculating-pi)
  * [One time pad](src/problems/one-time-pad)
  * [Roman to Integer](src/problems/roman-to-integer)
  * [Sort Colors](src/problems/sort-colors)
  * [Sort Characters By Frequency](src/problems/sort-characters-by-frequency)
  * [Reverse Words In a String](src/problems/reverse-words-in-a-string)
  * [Min Stack](src/problems/min-stack)
  * [Transpose Matrix](src/problems/transpose-matrix)
  * [First Recurring Character](src/problems/first-recurring-character)
  * [Two Sum](src/problems/two-sum)
  * [Best Time to Buy and Sell Stock II](src/problems/best-time-to-buy-sell-stock)
  * [Combination Sum IV](src/problems/combination-sum-iv)
  * [Fibonacci](src/problems/fibonacci/solution.go)
  * [Contains Duplicate](src/problems/contains-duplicate)
  * [Move Zeroes](src/problems/move-zeroes)
  * [Rotate Array](src/problems/rotate-array)

## Técnicas usadas

### Recursão
A recursão, em particular, está no coração não só de vários algoritmos, mas até mesmo em linguagens de programação completas.

Em algumas linguagens de programação funcional, como Scheme e Haskell, a recursão substitui os laços usados nas linguagens imperativas. Contudo, vale a pena lembrar que tudo que pode ser feito com uma técnica recursiva também pode sê-lo com uma técnica iterativa.


### Memoization
A memoization tem sido aplicada com sucesso para agilizar o trabalho dos parsers (programas que interpretam linguagens). É útil para todos os problemas nos quais o resultado de um cálculo recente será provavelmente solicitado de novo.

Outra aplicação da memoization está nos runtimes de linguagens. Alguns runtimes de linguagens (versões de Prolog, por exemplo) armazenam os resultados das chamadas de funções automaticamente (automemoization), de modo que a função não precisará executar da próxima vez que a mesma chamada for feita.

### Compactação
A compactação tem feito com que um mundo conectado pela internet com limitações de largura de banda seja mais tolerável.

A técnica de cadeia de bits pode ser usada para tipos de dados simples do mundo real que tenham um número limitado de valores possíveis, para os quais mesmo um byte poderia ser um exagero.

A maioria dos algoritmos de compactação, porém, atua encontrando padrões ou estruturas em um conjunto de dados, os quais permitem que informações repetidas sejam eliminadas.

## Big O

* Usado para realizar a comparação objetiva entre algorítimos
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

## Latency numbers every programmer should know

```
Latency Comparison Numbers
--------------------------
L1 cache reference                           0.5 ns
Branch mispredict                            5   ns
L2 cache reference                           7   ns                      14x L1 cache
Mutex lock/unlock                           25   ns
Main memory reference                      100   ns                      20x L2 cache, 200x L1 cache
Compress 1K bytes with Zippy            10,000   ns       10 us
Send 1 KB bytes over 1 Gbps network     10,000   ns       10 us
Read 4 KB randomly from SSD*           150,000   ns      150 us          ~1GB/sec SSD
Read 1 MB sequentially from memory     250,000   ns      250 us
Round trip within same datacenter      500,000   ns      500 us
Read 1 MB sequentially from SSD*     1,000,000   ns    1,000 us    1 ms  ~1GB/sec SSD, 4X memory
HDD seek                            10,000,000   ns   10,000 us   10 ms  20x datacenter roundtrip
Read 1 MB sequentially from 1 Gbps  10,000,000   ns   10,000 us   10 ms  40x memory, 10X SSD
Read 1 MB sequentially from HDD     30,000,000   ns   30,000 us   30 ms 120x memory, 30X SSD
Send packet CA->Netherlands->CA    150,000,000   ns  150,000 us  150 ms

Notes
-----
1 ns = 10^-9 seconds
1 us = 10^-6 seconds = 1,000 ns
1 ms = 10^-3 seconds = 1,000 us = 1,000,000 ns
```

Handy metrics based on numbers above:

* Read sequentially from HDD at 30 MB/s
* Read sequentially from 1 Gbps Ethernet at 100 MB/s
* Read sequentially from SSD at 1 GB/s
* Read sequentially from main memory at 4 GB/s
* 6-7 world-wide round trips per second
* 2,000 round trips per second within a data center

### Latency numbers visualized

![](assets/latency_numbers.png)

## Técnicas para resolução de problemas
- When you got the problem, write down the key points at the top (i.e. sorted array). Make sure you have all the details.
- Make sure you double check: What are the inputs? What are the outputs?
- What is the most important value of the problem? Do you have time, and space and memory, etc.. What is the main goal?
- Start with the naive/brute force approach. First thing that comes into mind. It shows that you’re able to think well and critically (you don't need to write this code, just speak about it)
- Tell them why this approach is not the best (i.e. O(n^2) or higher, not readable, etc...)
- Start actually writing your code now. Keep in mind that the more you prepare and understand
what you need to code, the better the whiteboard will go. So never start a whiteboard
interview not being sure of how things are going to work out. That is a recipe for disaster.
- Test your code: Check for no params, 0, undefined, null, massive arrays, async code, etc

## Good code checklist:
- [✅] It works
- [✅] Good use of data structures
- [✅] Code Re-use/ Do Not Repeat Yourself
- [✅] Modular - makes code more readable, maintainable and testable
- [✅] Less than O(N^2). We want to avoid nested loops if we can since they are expensive. Two separate loops are better than 2 nested loops
- [✅] Low Space Complexity --> Recursion can cause stack overflow, copying of large arrays may
exceed memory of machine

## Heurestics to solve coding problems:
- [✅] Hash Maps are usually the answer to improve Time Complexity
- [✅] If it's a sorted array, use Binary tree to achieve O(log N). Divide and Conquer - Divide a data set
into smaller chunks and then repeating a process with a subset of data. Binary search is a great example of this
- [✅] Try Sorting your input
- [✅] Hash tables and precomputed information (i.e. sorted) are some of the best ways to optimize your code
- [✅] Look at the Time vs Space tradeoff. Sometimes storing extra state in memory can help the time.
- [✅] Space time tradeoffs: Hashtables usually solve this a lot of the times. You use more space, but you
can get a time optimization to the process. In programming, you often times can use up a little bit more space to get faster time


### Referências

- [System design primer](https://github.com/donnemartin/system-design-primer)
- [Estruturas de dados e algoritmos no YouTube](https://www.youtube.com/playlist?list=PLLXdhg_r2hKA7DPDsunoDZ-Z769jWn4R8)
- [Estrutura de Dados e Algoritmos em JavaScript](https://github.com/trekhleb/javascript-algorithms/blob/master/README.md)
- [Latency numbers every programmer should know](https://gist.github.com/hellerbarde/2843375)
>>>>>>> Stashed changes
