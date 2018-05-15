numbers = list(map(int, input().split()))
sortedNumbers = sorted(numbers)
print(sum([sortedNumbers[i] for i in range(4)]), sum([sortedNumbers[i] for i in range(1,5)]))