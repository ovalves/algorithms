# Torre de Hanoi

Três pinos verticais (daí o nome “torres”) encontram-se de pé.
Nós os chamaremos de A, B e C.

Discos em formato de rosquinhas estão na torre A. O disco maior está embaixo, e nós o chamaremos de disco 1. Os demais discos acima do disco 1 recebem números crescentes e são cada vez menores. Por exemplo, se trabalhássemos com três discos, o disco maior, que está embaixo, seria o disco 1. O próximo disco maior, o disco 2, estaria sobre o disco 1. Por fim, o disco menor, o disco 3, estaria sobre o disco 2.

Nosso objetivo é mover todos os discos da torre A para a torre C, dadas as seguintes restrições:
* Somente um disco pode ser movido por vez.
* O disco mais acima em qualquer torre é o único disponível para ser movido.
* Um disco maior não pode estar em cima de um disco menor.

![Hanoi](../../../assets/hanoi.png)

## Solucionando as Torres de Hanói

Como as Torres de Hanói podem ser resolvidas?

Suponha que estamos tentando mover apenas um disco. Saberíamos como fazer isso, certo? De fato, mover um disco é o nosso caso de base para uma solução recursiva das Torres de Hanói.

O caso recursivo é mover mais de um disco. Assim, o principal insight é o fato de termos, basicamente, dois cenários para os quais devemos escrever um código: mover um disco (o caso de base) e mover mais de um disco (o caso recursivo).