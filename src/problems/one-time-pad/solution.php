<?php

/**
 * Gera um token randomico (pad) e um token cipher a partir dos dados da string original
 *
 * @param string $plaintext
 * @return array
 */
function encrypt(string $plaintext) : array
{
    $pad = bin2hex(random_bytes(strlen($plaintext)));
    $cipher = bin2hex($plaintext ^ $pad); # XOR

    return [$pad, $cipher];
}

/**
 * Retorna o plaintext de acordo com a
 * combinação XOR do token randomico (pad) e do token gerado a partir da string original
 *
 * @param string $pad
 * @param string $cipher
 * @return string
 */
function decrypt(string $pad, string $cipher) : string
{
    return $pad ^ hex2bin($cipher); # XOR
}

/* ========================================================== */
list($pad, $cipher) = encrypt("One Time Pad!");
echo decrypt($pad, $cipher);
