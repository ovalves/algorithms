<?php
/*
Example 1:
    Input: nums1 = [1,3], nums2 = [2]
    Output: 2.00000
    Explanation: merged array = [1,2,3] and median is 2.

Example 2:
    Input: nums1 = [1,2], nums2 = [3,4]
    Output: 2.50000
    Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Example 3:
    Input: nums1 = [0,0], nums2 = [0,0]
    Output: 0.00000

Example 4:
    Input: nums1 = [], nums2 = [1]
    Output: 1.00000

Example 5:
    Input: nums1 = [2], nums2 = []
    Output: 2.00000
*/

class Solution {

    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @return Float
     */
    function findMedianSortedArrays($nums1, $nums2) {
        $merged = array_merge($nums1, $nums2);
        sort($merged);
        $len = count($merged);
        $pos = $len / 2;

        if ($len % 2 == 0) {
            return ($merged[$pos] + $merged[$pos - 1]) / 2;
        }

        return floor($merged[$pos]);
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

$solution = new Solution;
$key = 0;

array_map(function() use (&$key, $tests, $solution) {
    echo $solution->findMedianSortedArrays(
        $tests[$key][0],
        $tests[$key][1]
    ) . PHP_EOL;
    $key++;
}, $tests);
