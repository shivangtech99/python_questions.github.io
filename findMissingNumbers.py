def findMissingNumbers(n):
    numbers = set(n)
    length = len(n)
    output = []
    for i in range(1, n[-1]):
        if i not in numbers:
            output.append(i)
    return output


listOfNumbers = [1,2,3,4,6,7,10]
print(findMissingNumbers(listOfNumbers))
