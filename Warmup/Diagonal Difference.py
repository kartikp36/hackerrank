size = int(input())
elements = []
sum1=0
sum2=0
total=0
for i in range(size):
    elements.append(list(map(int, input().split())))
    sum1 += elements[i][i]
    sum2 += elements[i][size-i-1]
total=sum1-sum2
if total<0 :
    total=0-total

print(total)