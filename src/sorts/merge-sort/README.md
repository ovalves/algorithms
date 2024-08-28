# Merge sort

O merge sort, ou ordenação por mistura, é um exemplo de algoritmo de ordenação por comparação do tipo dividir-para-conquistar.

Sua ideia básica consiste em Dividir (o problema em vários subproblemas e resolver esses subproblemas através da recursividade) e Conquistar (após todos os subproblemas terem sido resolvidos ocorre a conquista que é a união das resoluções dos subproblemas). Como o algoritmo Merge Sort usa a recursividade, há um alto consumo de memória e tempo de execução, tornando esta técnica não muito eficiente em alguns problemas.

```
Representação da ordenação com merge sort.
```
![Sorting](https://upload.wikimedia.org/wikipedia/commons/c/c5/Merge_sort_animation2.gif)

```
Exemplo da ordenação com merge sort.
```
![Sorting_Example](https://upload.wikimedia.org/wikipedia/commons/c/cc/Merge-sort-example-300px.gif)

### Exemplo de código
```python
def merge_sort(lista):
    if len(lista) > 1:
        split = len(lista)//2
        leftVector = lista[:split].copy()
        rightVector = lista[split:].copy()

        merge_sort(leftVector)
        merge_sort(rightVector)

        i = j = k = 0

        # Ordena leftVector e rightVector
        while i < len(leftVector) and j < len(rightVector):
            if leftVector[i] < rightVector[j]:
                lista[k] = leftVector[i]
                i += 1
            else:
                lista[k] = rightVector[j]
                j += 1
            k += 1

        # Ordenação final
        while i < len(leftVector):
            lista[k] = leftVector[i]
            i += 1
            k += 1

        while j < len(rightVector):
            lista[k] = rightVector[j]
            j += 1
            k += 1

    return lista

merge_sort([12, 31, 5, 3, 0, 43, 99, 78, 32, 9, 7])
```

```
Visualização on-line
```
- [visualgo](https://visualgo.net/en/sorting)


## Referência

- [Wikipedia](https://en.wikipedia.org/wiki/Merge_sort)