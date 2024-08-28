# A pesquisa binária

A pesquisa ou busca binária é um algoritmo de busca em vetores que segue o paradigma de divisão e conquista.
Ela parte do pressuposto de que o vetor está ordenado e realiza sucessivas divisões do espaço de busca
comparando o elemento buscado (chave) com o elemento no meio do vetor. Se o elemento do meio do vetor for a chave,
a busca termina com sucesso. Caso contrário, se o elemento do meio vier antes do elemento buscado,
então a busca continua na metade posterior do vetor. E finalmente, se o elemento do meio vier depois da chave,
a busca continua na metade anterior do vetor.

Vamos supor que você esteja procurando o nome de uma pessoa em uma agenda telefônica (que frase antiquada!).
O nome começa com K. Você pode começar na primeira página da agenda e ir folheando até chegar aos Ks.
Porém você provavelmente vai começar pela metade, pois sabe que os Ks estarão mais perto dali.

```
Representação da busca binária, onde o número a ser buscado é o 7.
```
![Binary_Search](https://upload.wikimedia.org/wikipedia/commons/8/83/Binary_Search_Depiction.svg)

## Referência

- [Wikipedia](https://en.wikipedia.org/wiki/Binary_search_algorithm)