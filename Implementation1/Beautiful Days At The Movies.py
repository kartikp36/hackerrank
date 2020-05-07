inputs = list(map(int,input().split()))
i = inputs[0]
j = inputs[1]
k = inputs[2]

beautifulDays = 0
for i in range(i,j+1):
    x = abs(i - int(''.join(reversed(str(i)))))
    if x % k == 0:
        beautifulDays += 1
print(beautifulDays)
