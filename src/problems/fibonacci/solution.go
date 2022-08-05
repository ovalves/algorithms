package main

import "fmt"

func main() {
	fmt.Println("Fib -> 5:", fib(5))
	fmt.Println("Fib -> 10:", fib(10))
	fmt.Println("Fib -> 12:", fib(12))
}

func fib(n int) int {
	if n < 2 {
		return n
	}

	return fib(n-2) + fib(n-1)
}
