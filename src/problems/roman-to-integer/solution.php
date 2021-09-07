<?php

class Solution
{
    /**
     * @param String $s
     * @return Integer
     */
    public function romanToInt(string $s)
    {
        $symbols = [
            'I' => 1,
            'V' => 5,
            'X' => 10,
            'L' => 50,
            'C' => 100,
            'D' => 500,
            'M' => 1000,
        ];

        $result = 0;
        $prev = null;
        $list = str_split(strrev($s), 1);
        foreach ($list as $key => $letter) {
            if (isset($list[$key - 1])) {
                $prev = $list[$key - 1];
            }
            if ($result <= $symbols[$letter] || $prev == $letter) {
                $result += $symbols[$letter];
                continue;
            }
            $result -= $symbols[$letter];
        }

        return $result;
    }
}
