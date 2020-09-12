# Lista ligada

Uma lista ligada ou lista encadeada é uma estrutura de dados linear e dinâmica.
Ela é composta por células que apontam para o próximo elemento da lista. Para "ter" uma lista ligada/encadeada,
basta guardar seu primeiro elemento, e seu último elemento aponta para uma célula nula.
O esquema a seguir representa uma lista ligada/encadeada com 5 elementos:

```
Célula 1 ---> Célula 2 ---> Célula 3 ---> Célula 4 ---> Célula 5 ---> (Nulo)
```

Para inserir dados ou remover dados é necessário ter um ponteiro que aponte para o 1º elemento e outro que aponte para o fim,
porque se quisermos inserir ou apagar dados que estão nessas posições, a operação será rapidamente executada.
Caso seja necessário editar um nó que esteja no meio da lista será feita uma busca pela posição desejada.

## Vantagens
* A inserção ou remoção de um elemento na lista não implica a mudança de lugar de outros elementos;
* Não é necessário definir, no momento da criação da lista, o número máximo de elementos que esta poderá ter. Ou seja, é possível alocar memória "dinamicamente", apenas para o número de nós necessários.

## Desvantagens
* A manipulação torna-se mais "perigosa" uma vez que, se o encadeamento (ligação) entre elementos da lista for mal feito, toda a lista pode ser perdida;
* Para aceder ao elemento na posição n da lista, deve-se percorrer os n - 1 anteriores.

## Níveis de complexidade

Numa lista com n itens, temos as seguintes complexidades de tempo no pior caso:

* Inserção
    * Cabeça da lista O(1)
    * Cauda da lista O(n) (O(1) quando se tem uma referência pro fim da lista)
    * Meio O(n)

* Exclusão
    * Cabeça da lista O(1)
    * Cauda da lista O(n) (O(1) quando se tem uma referência pro fim da lista)
    * Meio O(n)

```
Representação da lista ligada.
```
![Singly-linked-list](https://upload.wikimedia.org/wikipedia/commons/6/6d/Singly-linked-list.svg)

## Referência

- [Wikipedia](https://en.wikipedia.org/wiki/Linked_list)