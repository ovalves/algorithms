def fib2(n: int) -> int:
    if n < 2:
        return n

    return fib2(n - 2) + fib2(n - 1)

if __name__ == "__main__":
    print(f"Fib -> 5: {fib2(5)}")
    print(f"Fib -> 10: {fib2(10)}")
    print(f"Fib -> 12: {fib2(12)}")