def binary_search(numbers, targetNumber):
    lowerLimit = 0
    upperLimit = len(numbers) - 1

    while lowerLimit <= upperLimit:
        middleNumber = int((lowerLimit + upperLimit) / 2)
        if numbers[middleNumber] == targetNumber:
            return middleNumber

        if numbers[middleNumber] > targetNumber:
            upperLimit = middleNumber - 1
        else:
            lowerLimit = middleNumber + 1
    return None # None => Número não encontrado na lista

numbers = [1, 3, 4, 6, 7, 8, 10, 13, 14, 18, 19, 21, 24, 37, 40, 45, 71]
print(f"Número de iterações: {binary_search(numbers, 7)}")
print(f"Número de iterações: {binary_search(numbers, -1)}")