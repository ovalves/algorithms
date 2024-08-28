# Quick sort

O algoritmo quicksort é um método de ordenação muito rápido e eficiente, inventado por C.A.R. Hoare em 1960, quando visitou a Universidade de Moscovo como estudante. Naquela época, Hoare trabalhou em um projeto de tradução de máquina para o National Physical Laboratory. Ele criou o quicksort ao tentar traduzir um dicionário de inglês para russo, ordenando as palavras, tendo como objetivo reduzir o problema original em subproblemas que possam ser resolvidos mais fácil e rápido. Foi publicado em 1962 após uma série de refinamentos.

O quicksort é um algoritmo de ordenação por comparação não-estável.

### O algoritmo computacional
O quicksort adota a estratégia de divisão e conquista. A estratégia consiste em rearranjar as chaves de modo que as chaves "menores" precedam as chaves "maiores". Em seguida o quicksort ordena as duas sublistas de chaves menores e maiores recursivamente até que a lista completa se encontre ordenada. [3]Os passos são:

* Escolha um elemento da lista, denominado pivô;
* Particiona: rearranje a lista de forma que todos os elementos anteriores ao pivô sejam menores que ele, e todos os elementos posteriores ao pivô sejam maiores que ele. Ao fim do processo o pivô estará em sua posição final e haverá duas sub listas não ordenadas. Essa operação é denominada partição;
* Recursivamente ordene a sub lista dos elementos menores e a sub lista dos elementos maiores;

O caso base da recursão são as listas de tamanho zero ou um, que estão sempre ordenadas. O processo é finito, pois a cada iteração pelo menos um elemento é posto em sua posição final e não será mais manipulado na iteração seguinte.

A escolha do pivô e os passos do Particiona podem ser feitos de diferentes formas e a escolha de uma implementação específica afeta fortemente a performance do algoritmo.

```
Representação da ordenação com Quick Sort.
```
![Sorting](https://upload.wikimedia.org/wikipedia/commons/6/6a/Sorting_quicksort_anim.gif)

```
Exemplo da ordenação com Quick Sort.
```
![Sorting_Example](https://upload.wikimedia.org/wikipedia/commons/a/af/Quicksort-diagram.svg)

### Exemplo de código
```python
def partition(vector, start, end):
    pivot = vector[end]
    i = start - 1

    for j in range(start, end):
        if vector[j] <= pivot:
            i += 1
            vector[i], vector[j] = vector[j], vector[i]
    vector[i + 1], vector[end] = vector[end], vector[i + 1]
    return i + 1


def quick_sort(vector, start, end):
    if start < end:
        position = partition(vector, start, end)

        # Left Side
        quick_sort(vector, start, position - 1)

        # Right Side
        quick_sort(vector, position + 1, end)
    return vector

vector = [12, 31, 5, 3, 0, 43, 99, 78, 32, 9, 7]
quick_sort(vector, 0, len(vector) - 1)
```

```
Visualização on-line
```
- [visualgo](https://visualgo.net/en/sorting)

## Referência

- [Wikipedia](https://en.wikipedia.org/wiki/Quicksort)