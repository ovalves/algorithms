# Bubble sort

O bubble sort, ou ordenação por flutuação (literalmente "por bolha"), é um algoritmo de ordenação dos mais simples. A ideia é percorrer o vector diversas vezes, e a cada passagem fazer flutuar para o topo o maior elemento da sequência. Essa movimentação lembra a forma como as bolhas em um tanque de água procuram seu próprio nível, e disso vem o nome do algoritmo.

No melhor caso, o algoritmo executa n operações relevantes, onde n representa o número de elementos do vector. No pior caso, são feitas n^2 operações. A complexidade desse algoritmo é de ordem quadrática. Por isso, ele não é recomendado para programas que precisem de velocidade e operem com quantidade elevada de dados.

```
O algoritmo com 10 elementos faz 9 comparações na primeira passagem, 8 na segunda, 7 na terceira. Ou seja (n – 1, n – 2, n – 3, ...)
```

```
Representação da ordenação com bubble sort.
```
![Sorting](https://upload.wikimedia.org/wikipedia/commons/3/37/Bubble_sort_animation.gif)

```
Exemplo da ordenação com bubble sort.
```
![Sorting_Example](https://upload.wikimedia.org/wikipedia/commons/c/c8/Bubble-sort-example-300px.gif)

```
Visualização on-line
```
- [visualgo](https://visualgo.net/en/sorting)


## Referência

- [Wikipedia](https://en.wikipedia.org/wiki/Bubble_sort)