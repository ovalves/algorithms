package main

import (
	"fmt"
)

func main() {
	// result: 0
	// prices := []int{1}

	// result: 1
	prices := []int{1, 2}

	// result: 7
	// prices := []int{7, 1, 5, 3, 6, 4}

	// result: 0
	// prices := []int{7, 6, 4, 3, 1}

	// result: 4
	// prices := []int{1, 2, 3, 4, 5}

	// result: 2
	// prices := []int{9, 11, 7, 5, 3}

	// result: 8
	// prices := []int{31, 2, 4}

	// result: 11
	// prices := []int{3, 11, 7, 10, 3}

	// result: 13
	// prices := []int{3, 11, 5, 10, 3}

	// result: 0
	// prices := []int{0, 0, 0, 0, 0}

	// result: 0
	// prices := []int{2, 0, 0, 0, 0}

	profit := maxProfit(prices)

	fmt.Println("Profit: ", profit)
}

func maxProfit(prices []int) int {
	profit := 0

	if len(prices) <= 1 {
		return profit
	}

	for k, buyPrice := range prices {
		_profit := 0
		for _, price := range prices[k+1:] {
			sell := price - buyPrice

			if _profit > sell {
				profit += _profit
				break
			}

			profit += sell
			break

		}
	}

	return profit
}
