input()
theNumbers = input().split()

for i in range(len(theNumbers)):
	theNumbers[i] = int(theNumbers[i])

print(sum(theNumbers))