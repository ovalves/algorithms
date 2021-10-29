package main

import (
	"fmt"
)

func main() {
	nums := []int{2,0,2,1,1,0}
	res := sortColors(nums)

	fmt.Printf("%v", res)
}

func sortColors(nums []int) []int {
	fmt.Println(len(nums))


	len := len(nums)

	if len <= 1 {
		return nums
	}

	for left := 0; left < len; left++ {
		for right := 0; right < len; right++ {
			if nums[right] <= nums[left] {
				continue
			}

			nums[left], nums[right] = nums[right], nums[left];
		}
	}

	return nums
}