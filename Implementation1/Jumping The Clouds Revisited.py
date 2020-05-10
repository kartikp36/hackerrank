inputs = list(map(int, input().split()))
n = inputs[0]
k = inputs[1]
clouds = list(map(int, input().split()))
e = 100
i = 0
while i != n:
    if clouds[i] == 0:
        e -= 1
    else:
        e -= 3
    i += k
print(e)
