# Shell sort

Shell sort é o mais eficiente algoritmo de classificação dentre os de complexidade quadrática. É um refinamento do insertion sort. O algoritmo difere do método de insertion sort pelo fato de no lugar de considerar a lista a ser ordenado como um único segmento, ele considera vários segmentos sendo aplicado o método de insertion sort. Basicamente o algoritmo passa várias vezes pela lista dividindo-a em listas menores. Nas listas menores é aplicado o método de insertion sort.

### Funcionamento

* O vetor original é quebrado em subvetores
* Cada subvetor é ordenado
  * Os valores do subvetor são comparados e trocados
* Ao final da rodada de comparação, o subvetor é quebrado em mais partes e todo o processo é repetido

```
Representação da ordenação com shell sort.
```
![Sorting](https://upload.wikimedia.org/wikipedia/commons/d/d8/Sorting_shellsort_anim.gif)

```
Visualização on-line
```
- [usfca](https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html)

## Referência

- [Wikipedia](https://en.wikipedia.org/wiki/Shellsort)