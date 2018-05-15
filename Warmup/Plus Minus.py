input()
numbers = list(map(int,input().split()))
positive = 0
negative = 0
zeros = 0
for i in numbers :
	if  i > 0 :
		positive += 1
	elif  i < 0 :
		negative += 1
	else:
		zeros += 1
print(positive / len(numbers))
print(negative / len(numbers))
print(zeros / len(numbers))