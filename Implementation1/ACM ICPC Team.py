inputs = list(map(int,input().split()))
n = inputs[0]
m = inputs[1]
person = [input() for _ in range(n)]
topics = []
for i in range(n):
    for j in range(i+1,n):
        t = bin(int(person[i],2) | int(person[j],2))
        topics.append(t.count('1'))
print(max(topics))
print(topics.count(max(topics)))
