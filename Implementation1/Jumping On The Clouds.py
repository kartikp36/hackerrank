l = int(input())
clouds = list(map(int, input().split()))
step = 0
skip = 0
# 1st cloud must be 0(safe)
for s in range(0, l - 1):
    if clouds[s] == 0:
        if skip == 1:
            skip = 0
            continue
        elif (s < l-2) and (clouds[s + 1] == 0 and clouds[s + 2] == 0) :
            step += 1
            skip = 1
        else:
            step += 1

print(step)
