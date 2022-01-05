<?php

class MinStack
{
    private $matrix;
    private $matrixPosition;

    /**
     */
    public function __construct()
    {
        $this->matrix = [];
        $this->matrixPosition = -1;
    }

    /**
     * @param Integer $val
     * @return NULL
     */
    public function push($val)
    {
        $this->matrixPosition++;
        $this->matrix[$this->matrixPosition] = $val;
    }

    /**
     * @return NULL
     */
    public function pop()
    {
        unset($this->matrix[$this->matrixPosition]);
        $this->matrixPosition--;
    }

    /**
     * @return Integer
     */
    public function top()
    {
        return (int) $this->matrix[$this->matrixPosition];
    }

    /**
     * @return Integer
     */
    public function getMin()
    {
        return (int) min($this->matrix);
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * $obj = MinStack();
 * $obj->push($val);
 * $obj->pop();
 * $ret_3 = $obj->top();
 * $ret_4 = $obj->getMin();
 */
$minStack = new MinStack();
$minStack->push(-2);
$minStack->push(0);
$minStack->push(-3);
echo 'min ' . $minStack->getMin() . PHP_EOL; // return -3
$minStack->pop();
echo 'top ' . $minStack->top() . PHP_EOL;    // return 0
echo 'min ' . $minStack->getMin() . PHP_EOL; // return -2
