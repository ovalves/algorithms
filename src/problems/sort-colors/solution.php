<?php

class Solution
{

    /**
     * @param Integer[] $nums
     * @return NULL
     */
    public function sortColors(&$nums)
    {
        $len = count($nums);

        if ($len <= 1) {
            return $nums;
        }

        for ($left = 0; $left < $len; $left++) {
            for ($right = 0; $right < $len; $right++) {
                if ($nums[$right] <= $nums[$left]) {
                    continue;
                }

                list($nums[$left], $nums[$right]) = [$nums[$right], $nums[$left]];
            }
        }

        return $nums;
    }
}

$nums1 = [2,0,2,1,1,0];
echo "SOL 1 => " . PHP_EOL;
print_r((new Solution)->sortColors($nums1)) . PHP_EOL;

$numm2 = [2,0,1];
echo "SOL 2 => " . PHP_EOL;
print_r((new Solution)->sortColors($numm2)) . PHP_EOL;

$nums3 = [0];
echo "SOL 3 => " . PHP_EOL;
print_r((new Solution)->sortColors($nums3)) . PHP_EOL;

$nums4 = [1];
echo "SOL 4 => " . PHP_EOL;
print_r((new Solution)->sortColors($nums4)) . PHP_EOL;

$nums5 = [1, 0];
echo "SOL 5 => " . PHP_EOL;
print_r((new Solution)->sortColors($nums5)) . PHP_EOL;

$nums6 = [0, 1];
echo "SOL 6 => " . PHP_EOL;
print_r((new Solution)->sortColors($nums6)) . PHP_EOL;

$nums7 = [0, 1, 2];
echo "SOL 7 => " . PHP_EOL;
print_r((new Solution)->sortColors($nums7)) . PHP_EOL;

$nums8 = [1, 2, 1, 2, 0, 1, 2, 0 , 2, 0, 1, 0, 1, 2, 1, 2];
echo "SOL 8 => " . PHP_EOL;
print_r((new Solution)->sortColors($nums8)) . PHP_EOL;
