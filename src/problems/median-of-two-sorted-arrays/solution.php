<?php

class Solution
{
    /**
     * @param  int[] $nums1
     * @param  int[] $nums2
     * @return float
     */
    public function findMedianSortedArrays(array $nums1, array $nums2)
    {
        $merged = array_merge($nums1, $nums2);
        sort($merged);

        $len = count($merged);
        $median = $len / 2;

        if (0 == $len % 2) {
            return ($merged[$median] + $merged[$median - 1]) / 2;
        }

        return floor($merged[$median]);
    }
}

$tests = [
    '0' => [
        [3],
        [-3,-2, -52]
    ],
    '1' => [
        [2, 0],
        [0, 0]
    ],
    '2' => [
        [],
        [1,2,3,4,5]
    ],
    '3' => [
        [12, 3, 3],
        [9, 15, 2]
    ],
    '4' => [
        [2],
        []
    ],
    '5' => [
        [],
        [1]
    ],
    '6' => [
        [],
        [2, 3]
    ],
];

$solution = new Solution();
$key = 0;

array_map(function () use (&$key, $tests, $solution) {
    echo "Test {$key} = " . $solution->findMedianSortedArrays(
        $tests[$key][0],
        $tests[$key][1]
    ) . PHP_EOL;
    $key++;
}, $tests);
