package main
import "fmt"

func Reverse(s string) string {
    runes := []rune(s)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}

func romanToInt(s string) int {
	symbols := make(map[string]int)

	symbols["I"] = 1
	symbols["V"] = 5
	symbols["X"] = 10
	symbols["L"] = 50
	symbols["C"] = 100
	symbols["D"] = 500
	symbols["M"] = 1000

	var result int = 0

	for pos, char := range s {

		value, exists := symbols[string(char)]

		fmt.Printf("key exists in map: %t, value: %v \n", exists, pos)

		result -= value
	}

	return result
}

func main() {
	res := romanToInt("IVX")
	fmt.Printf("Resultado: %f", res)
}