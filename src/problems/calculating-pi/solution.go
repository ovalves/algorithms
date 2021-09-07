package main
import "fmt"

func calculatePI(terms int) float64 {
	var numerator float64 = 4.0
	var denominator float64 = 1.0
	var operation float64 = 1.0
	var pi float64 = 0.0

	for i := 0; i <= terms; i++ {
		pi += operation * (numerator / denominator);
        denominator += 2.0
        operation *= -1.0
	}

	return pi
}

func main() {
	res := calculatePI(100000)
    fmt.Printf("Resultado: %f", res)
}