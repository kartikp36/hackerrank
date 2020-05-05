t = int(input())

for _ in range(t):
    s = 0
    first = list(map(int,input().split()))
    n = first[0]
    k = first[1]
    studs = list(map(int,input().split()))
    for i in studs:
         if i <= 0:
             s += 1
    if s >= k:
        print("NO")
    else:
        print("YES")
