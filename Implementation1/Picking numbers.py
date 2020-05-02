total = int(input())
numbers = list(map(int,input().split()))
numberset = list(set(numbers))
answers = []
for i in range(len(numberset)-1) :
    answers.append(numbers.count(numberset[i]))
    if abs(numberset[i] - numberset[i+1]) <= 1 :
       answers.append(numbers.count(numberset[i]) + numbers.count(numberset[i+1]))
if numbers.count(numbers[0]) == total :
    print(total)
else :
    print(max(answers))