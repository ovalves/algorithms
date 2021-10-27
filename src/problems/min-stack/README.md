Min Stack
====

> Site [LeetCode](https://leetcode.com/problems/min-stack/)

> Level Easy

## Description

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

    MinStack() initializes the stack object.
    void push(int val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.


Example 1:
```bash
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
```

Constraints:

- -231 <= val <= 231 - 1
- Methods pop, top and getMin operations will always be called on non-empty stacks.
- At most 3 * 104 calls will be made to push, pop, top, and getMin.


## Solution
> Language: PHP

```php
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
```