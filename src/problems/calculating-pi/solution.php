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
