everything = list(map(int,input().split()))
dollars = everything[0]
totalK = everything[1]
totalU = everything[2]
sums = []
keyboards = list(map(int,input().split()))
mouses = list(map(int,input().split()))
for k in keyboards :
    for m in mouses :
        if k + m <= dollars :
            sums.append(k+m)
if sums == [] : print("-1")
else : print(max(sums))