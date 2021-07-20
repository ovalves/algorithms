Fórmula de Leibniz para π
====

> Level Easy

> [wikipedia](https://pt.wikipedia.org/wiki/F%C3%B3rmula_de_Leibniz_para_%CF%80)

## Description

Em matemática, a fórmula de Leibniz para π, que leva o nome de Gottfried Wilhelm Leibniz, estabelece que

![Leibniz para π](/assets/calculating-pi/pi-1.svg)

Usando a notação de somatório:

![Leibniz para π](/assets/calculating-pi/pi-2.svg)

## Ineficiência

A fórmula converge lentamente. Para calcular π com 10 dígitos decimais corretos usando soma direta são necessários aproximadamente 5 bilhões de termos.

Contudo, a fórmula de Leibniz pode ser usada para calcular π com grande precisão usando várias técnicas de aceleração de convergência.


## Solution
> Language: PHP

```php
<?php

/**
 * Fórmula de Leibniz para π (PI)
 *
 * @param int $terms
 * @return float
 */
function calculatePI(int $terms = 1000): float
{
    $numerator = 4.0;
    $denominator = 1.0;
    $operation = 1.0;
    $pi = 0.0;

    for ($i=0; $i <= $terms; $i++) {
        $pi += $operation * ($numerator / $denominator);
        $denominator += 2.0;
        $operation *= -1.0;
    }
    return $pi;
}

echo calculatePI(100000);
```