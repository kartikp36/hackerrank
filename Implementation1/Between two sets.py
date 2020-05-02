lengths = list(map(int, input().split()))
n = lengths[0]
m = lengths[1]
listA = list(map(int, input().split()))
listB = list(map(int, input().split()))

answer = []
counts = 0

for x in range(max(listA), min(listB) + 1):
    for j in listA:
        if x % j != 0:
            break
        elif j == listA[n-1]:
            answer.append(x)

for y in answer:
    for k in listB:
        if k % y != 0:
            break
        elif k == listB[m-1]:
            counts += 1

print(counts)
