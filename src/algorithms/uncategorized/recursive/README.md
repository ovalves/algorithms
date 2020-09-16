# Recursividade

Um método comum de simplificação é dividir o problema em subproblemas do mesmo tipo. Como técnica de programação, este método é conhecido como dividir e conquistar e é a chave para a construção de muitos algoritmos importantes, bem como uma parte fundamental da programação dinâmica.

A recursão na programação é bem exemplificada quando uma função é definida em termos de si mesma. Um exemplo da aplicação da recursão são os parsers (analisadores gramaticais) para linguagens de programação. Uma grande vantagem da recursão é que um conjunto infinito de sentenças possíveis, designs ou outros dados podem ser definidos, analisados ou produzidos por um programa de computador finito.

Relações de recorrência são equações que definem uma ou mais sequências recursivamente. Alguns tipos específicos de relações de recorrência podem ser “resolvidos” para que se obtenha uma definição não-recursiva.

Um exemplo clássico de recursão é a definição da função fatorial, dada aqui em pseudocódigo:

```
função fatorial(n) {
    se (n <= 1)
        retorne 1;
    senão
        retorne n * fatorial(n - 1);
}
```

## Referência

- [Wikipedia](https://en.wikipedia.org/wiki/Recursion#In_computer_science)