<?php

class CompressedGene
{
    private int $bitString = 1;
    private int $originalGeneLength;
    private string $originalString;

    public function getCompressedSize()
    {
        return strlen($this->bitString) * 2;
    }

    public function getDecompressedString()
    {
        return $this->originalString;
    }

    public function compress(string $gene)
    {
        $this->originalGeneLength = (strlen($gene) * 2) - 2;
        $genes = array_map('strtoupper', str_split($gene));
        foreach ($genes as $nucleotide) {
            $this->bitString <<= 2;  // shift left two bits
            if ('A' == $nucleotide) {
                $this->bitString |= 0b00; // change last two bits to 00
            } elseif ('C' == $nucleotide) {
                $this->bitString |= 0b01; // change last two bits to 01
            } elseif ('G' == $nucleotide) {
                $this->bitString |= 0b10; // change last two bits to 10
            } elseif ('T' == $nucleotide) {
                $this->bitString |= 0b11; // change last two bits to 11
            } else {
                throw new Exception("Invalid Nucleotide:{$nucleotide}");
            }
        }
    }

    public function decompress()
    {
        $this->originalString = '';

        foreach (range(0, $this->originalGeneLength, 2) as $value) {
            $bits = $this->bitString >> $value & 0b11;  // get just 2 relevant bits
            if (0b00 == $bits) {
                $this->originalString .= 'A'; // A
            } elseif (0b01 == $bits) {
                $this->originalString .= 'C'; // C
            } elseif (0b10 == $bits) {
                $this->originalString .= 'G'; // G
            } elseif (0b11 == $bits) {
                $this->originalString .= 'T';  // T
            } else {
                throw new Exception("Invalid bits {$bits}");
            }
        }

        $this->originalString = strrev($this->originalString);
    }
}

$original = str_repeat(
    'ACTG',
    8
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
