# Selection sort

A ordenação por seleção (do inglês, selection sort) é um algoritmo de ordenação baseado em se passar sempre o menor valor do vetor para a primeira posição (ou o maior dependendo da ordem requerida), depois o de segundo menor valor para a segunda posição, e assim é feito sucessivamente com os n − 1 elementos restantes, até os últimos dois elementos.

```
Melhora a ordenação em relação ao bubble sort reduzindo o número de trocas necessárias de n^2 para n
```

```
Representação da ordenação com selection sort.
```
![Sorting](https://upload.wikimedia.org/wikipedia/commons/b/b0/Selection_sort_animation.gif)

```
Exemplo da ordenação com selection sort.
```
![Sorting_Example](https://upload.wikimedia.org/wikipedia/commons/9/94/Selection-Sort-Animation.gif)

### Exemplo de código
```python
def selection_sort(lista):
    n = len(lista)

    for i in range(n):
        index_min_value = i
        for j in range(i + 1, n):
            if lista[index_min_value] > lista[j]:
                index_min_value = j

        temp = lista[i]
        lista[i] = lista[index_min_value]
        lista[index_min_value] = temp

    return lista

selection_sort([12, 31, 5, 3, 0, 43, 99, 78, 32, 9, 7])
```

```
Visualização on-line
```
- [visualgo](https://visualgo.net/en/sorting)


## Referência

- [Wikipedia](https://en.wikipedia.org/wiki/Selection_sort)