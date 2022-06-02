<?php

class Solution
{

    /**
     * @param Integer[][] $matrix
     * @return Integer[][]
     */
    public function transpose($matrix)
    {
        if (empty($matrix[0])) {
            return [];
        }

        list($rows, $cols) = [count($matrix), count($matrix[0])];
        $transMatrix = [];

        for ($i=0; $i < $rows; $i++) {
            for ($j=0; $j < $cols; $j++) {
                $transMatrix[$j][$i] = $matrix[$i][$j];
            }
        }

        return $transMatrix;
    }
}

/**
 * Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
 * Output: [[1,4,7],[2,5,8],[3,6,9]]
 */
print_r((new Solution)->transpose([[1,2,3],[4,5,6],[7,8,9]]));


/**
 * Input: matrix = [[1,2,3],[4,5,6]]
 * Output: [[1,4],[2,5],[3,6]]
 */
print_r((new Solution)->transpose([[1,2,3],[4,5,6]]));
