# Compactação trivial

Economizar espaço (virtual ou real) muitas vezes é importante. Usar menos espaço é mais eficiente, e é possível economizar dinheiro.

A compactação é o ato de tomar os dados e codificá-los (modificar o seu formato) de modo que ocupem menos espaço. A descompactação é o processo inverso, que faz com que os dados retornem ao seu formato original.

Há uma relação de custo-benefício entre tempo e espaço. Compactar uma porção de dados e descompactá-los de volta para o formato original exige tempo. Desse modo, a compactação de dados somente fará sentido em situações em que um tamanho menor tenha mais prioridade em relação a uma execução rápida. Pense em arquivos grandes sendo transmitidos pela internet. Compactá-los faz sentido, pois demorará mais para transferir os arquivos do que para descompactá-los depois que forem recebidos.

Os ganhos mais simples com a compactação de dados surgem quando você percebe que os tipos de dados armazenados usam mais bits do que são estritamente necessários para o seu conteúdo. Por exemplo, pensando no baixo nível, se um inteiro sem sinal que jamais excederia 65.535 é armazenado como um inteiro de 64 bits sem sinal na memória, ele está sendo armazenado de modo ineficiente. Esse dado poderia ser armazenado como um inteiro de 16 bits sem sinal. Isso reduziria o consumo de espaço do número propriamente dito em 75% (16 bits, em vez de 64 bits). Se milhões desses números forem armazenados de modo ineficiente, o espaço desperdiçado poderá totalizar megabytes.

Se o número de possíveis valores diferentes que um tipo deve representar for menor que o número de valores que os bits usados para armazená-lo podem representar, é provável que ele seja armazenado de modo mais eficiente. Considere os nucleotídeos que formam um gene no DNA.2 Cada nucleotídeo pode assumir apenas um entre quatro valores: A, C, G ou T.

No entanto, se o gene for armazenado como uma str, que pode ser imaginada como uma coleção de caracteres Unicode, cada nucleotídeo será representado por um caractere, o qual, em geral, exige 8 bits para armazenagem. Em binário, apenas 2 bits são necessários para armazenar um tipo com quatro valores possíveis: 00, 01, 10 e 11 são os quatro valores diferentes que podem ser representados por 2 bits. Se atribuirmos o valor 00 a A, 01 a C, 10 a G e 11 a T, a área de armazenagem necessária para uma string de nucleotídeos poderá ser reduzida em 75% (de 8 bits para 2 bits por nucleotídeo).

Em vez de armazenar nossos nucleotídeos como uma str, eles poderão ser armazenados como uma cadeia de bits. Uma cadeia de bits é exatamente o que parece ser: uma sequência de 1s e 0s de tamanho arbitrário.

![Trivial Compression](../../../assets/trivial_compression.png)

> Kopec, David. Problemas Clássicos de Ciência da Computação com Python (p. 31). Novatec Editora. Kindle Edition.

## Solution
> Language: PHP

```php
class CompressedGene
{
    private string $originalString;
    private array $bitStringArray = [];
    private array $stringCompressedSize = [];

    public function getCompressedSize(): int
    {
        return (int) array_sum($this->stringCompressedSize);
    }

    public function getDecompressedString(): string
    {
        return (string) $this->originalString;
    }

    public function compress(string $gene): void
    {
        $genes = array_map('strtoupper', str_split($gene, 32));

        foreach ($genes as $key => $gene) {
            $this->stringCompressedSize[$key] = (strlen($gene) * 2);
            $this->bitStringArray[$key] = 1;
            $gene = str_split($gene);

            foreach ($gene as $nucleotide) {
                $this->bitStringArray[$key] <<= 2;
                $this->bitStringArray[$key] |= match ($nucleotide) {
                    'C' => 0b01,
                    'G' => 0b10,
                    'T' => 0b11,
                    'A' => 0b00,
                };
            }
        }
    }

    public function decompress(): void
    {
        $this->originalString = '';

        foreach ($this->bitStringArray as $key => $bitString) {
            foreach (range(0, $this->stringCompressedSize[$key] - 2, 2) as $value) {
                $bits = $bitString >> $value & 0b11;
                $this->originalString .= match ($bits) {
                    0b01 => 'C',
                    0b10 => 'G',
                    0b11 => 'T',
                    0b00 => 'A',
                };
            }
        }

        $this->originalString = strrev($this->originalString);
    }
}
```