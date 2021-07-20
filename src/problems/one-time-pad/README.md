One-time pad
====

> Site [Wikipedia](https://pt.wikipedia.org/wiki/One-time_pad)

> Level Easy

## Description

One-time pad (OTP), em português cifra de uso único ou chave de uso único, é uma técnica de criptografia que não pode ser quebrada se utilizada corretamente.

Consiste num algoritmo em que o texto original é combinado, caractere por caractere, a uma chave secreta aleatória que para isso deve ter, no mínimo, o mesmo número de caracteres do texto original.

Para garantir que a criptografia seja segura, a chave só deve ser usada uma única vez, sendo imediatamente destruída após o uso.

## Solution
> Language: PHP

```php
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
```