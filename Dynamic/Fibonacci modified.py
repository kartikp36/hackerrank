i,j,n = list(map(int,input().split()))
terms = 2
while True:
    i = i+(j**2)
    terms += 1
    if terms == n:
        print(i)
        break
    j = j +(i**2)
    terms += 1
    if terms == n:
        print(j)
        break