<?php

class Solution
{
    /**
     * @param String $s
     * @return String
     */
    public function frequencySort($s)
    {
        $arr = array_count_values(str_split($s));
        arsort($arr);
        $text = '';
        array_walk($arr, function ($times, $char) use (&$text) {
            $text .= str_repeat($char, $times);
        });

        return $text;
    }
}

echo (new Solution)->frequencySort('tree') . PHP_EOL;
echo (new Solution)->frequencySort('cccaaa') . PHP_EOL;
echo (new Solution)->frequencySort('Aabb') . PHP_EOL;
echo (new Solution)->frequencySort('loveleetcode') . PHP_EOL;
