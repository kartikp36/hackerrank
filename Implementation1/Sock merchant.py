total = int(input())
socks = list(map(int,input().split()))
socks1 = set(socks)
frequency = []
answer = 0
for f in socks1 :
    frequency.append(socks.count(f))
for i in frequency :
    if i % 2 == 0 :
        answer += i/2
    else :
        answer += (i-1)/2
print(int(answer))