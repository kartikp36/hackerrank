total = int(input())
chocolates = list(map(int,input().split()))
birth = list(map(int,input().split()))
day = birth[0]
month = birth[1]
answer = 0
for i in range(total-month+1) :
    addition = 0
    for j in range(i,i+month) :
        addition += chocolates[j]
    if addition == day :
        answer += 1
print(answer)