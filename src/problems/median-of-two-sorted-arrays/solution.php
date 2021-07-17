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
