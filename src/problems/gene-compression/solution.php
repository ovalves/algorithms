<?php

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
                $bits = $bitString >> $value & 0b11;  // get just 2 relevant bits
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

$original = str_repeat(
    'ACTGACTGACTGACTGACTGACTGACTGACTGACTGACTGACTGACTG',
    115
);

$compress = new CompressedGene();

$originalSize = strlen($original) * 8;
echo "original size is: {$originalSize} bytes | original content is: {$original}\n";

$compress->compress($original);
$compressedSize = $compress->getCompressedSize();  // get compressed string

echo "compressed size is: {$compressedSize} bytes\n";

$compress->decompress();

$decompressed = $compress->getDecompressedString();

echo "original and decompressed are the same? \n";
var_dump($original == $decompressed);
var_dump($decompressed);
