#include<stdio.h>

float calculatePI(int terms)
{
    float numerator = 4.0;
    float denominator = 1.0;
    float operation = 1.0;
    float pi = 0.0;
    int i = 0;

    for (i = 0; i <= terms; i++) {
        pi += operation * (numerator / denominator);
        denominator += 2.0;
        operation *= -1.0;
    }

    return pi;
}

int main(void)
{
    printf("%f  ", calculatePI(1000));
    return 0;
}