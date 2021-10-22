<?php

class Solution
{
    /**
     * @param String $s
     * @return String
     */
    public function reverseWords($s)
    {
        return implode(" ", array_reverse(array_filter(explode(' ', trim($s)), function ($str) {
            return '' !== $str;
        })));
    }
}

/**
 * Resultado:
 *
 * pA S KipYyS0 GV9 7W8r q4 uM2P eLl sBmxVa1Eh lKw y5j02N M6FyWJ LFTT Aa vPKksW LDtzIOvWLt LKg3a 11lASBGl 0 i7 YgHsUKFd zIiIXd GsaSwLnOs glfOAYah40 TZH p L3jQ78 qM VBLWqIJXRi kT xmhQMptz qEjVjL UmNRei hQs 6eq 9v yY wUb6 en J kX WZJ0M3Z c W9Mqf7cep 15uAqvNl Jp nKCtoS8 aQ7iiTy OUVxX1zsUL KkkRVXY7 k0b9Ts QcspISw z o Rep6lU ZaYYygdFe sQ gtUGyw
 */
echo (new Solution)->reverseWords(
    " gtUGyw       sQ       ZaYYygdFe    Rep6lU  o z      QcspISw       k0b9Ts   KkkRVXY7   OUVxX1zsUL      aQ7iiTy      nKCtoS8       Jp  15uAqvNl   W9Mqf7cep    c      WZJ0M3Z       kX       J     en       wUb6 yY     9v      6eq hQs UmNRei   qEjVjL      xmhQMptz   kT     VBLWqIJXRi       qM      L3jQ78    p    TZH     glfOAYah40   GsaSwLnOs     zIiIXd     YgHsUKFd     i7      0       11lASBGl   LKg3a    LDtzIOvWLt   vPKksW Aa  LFTT      M6FyWJ  y5j02N      lKw sBmxVa1Eh     eLl uM2P  q4    7W8r   GV9    KipYyS0 S pA"
) . PHP_EOL;

/**
 * Resultado:
 *
 * world hello
 */
echo (new Solution)->reverseWords('  hello world  ') . PHP_EOL;

/**
 * Resultado:
 *
 * blue is sky the
 */
 echo (new Solution)->reverseWords('the sky is blue') . PHP_EOL;

/**
 * Resultado:
 *
 * example good a
 */
 echo (new Solution)->reverseWords('a good   example') . PHP_EOL;

/**
 * Resultado:
 *
 * Alice Loves Bob
 */
 echo (new Solution)->reverseWords('  Bob    Loves  Alice   ') . PHP_EOL;

/**
 * Resultado:
 *
 * bob like even not does Alice
 */
 echo (new Solution)->reverseWords('Alice does not even like bob') . PHP_EOL;
