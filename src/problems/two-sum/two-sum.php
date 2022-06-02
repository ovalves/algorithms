<?php

class Solution
{
    /**
     * @param array $nums
     * @param int $target
     * @return array
     */
    public function twoSum(array $nums, int $target): array
    {
        $len = count($nums);
        if ($len <= 2) {
            return array_keys($nums);
        }

        for ($i=0; $i < $len; $i++) {
            for ($j=$i + 1; $j < $len; $j++) {
                if (($nums[$i] + $nums[$j]) == $target) {
                    return [$i, $j];
                }
            }
        }
    }
}
