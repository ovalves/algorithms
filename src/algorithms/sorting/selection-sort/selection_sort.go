package main

import (
	"fmt"
)

func selectionSort(lista []int) []int {
	n := len(lista)
	var index_min_value int

	for i, v := range lista {
		index_min_value = i
		for j := i + 1; j < n; j++ {
			if lista[index_min_value] > lista[j] {
				index_min_value = j
			}
		}

        lista[i] = lista[index_min_value]
        lista[index_min_value] = v
	}

	return lista
}

func main()  {
	list := []int{12, 31, 5, 3, 0, 43, 99, 78, 32, 9, 7}
	sorted := selectionSort(list)
	fmt.Println(sorted)
}