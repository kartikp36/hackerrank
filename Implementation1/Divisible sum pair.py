myarray = list(map(int,input().split()))
total = myarray[0]
knumber = myarray[1]
numbers = list(map(int,input().split()))
answer = 0
for i in range(total) :
    for j in range(i,total) :
        if i<j and(numbers[i] + numbers[j]) % knumber == 0 :
            answer += 1
print(answer)