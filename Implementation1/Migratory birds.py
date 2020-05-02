int(input())
bird = list(map(int, input().split()))

types = list(set(bird))
counts = [bird.count(i) for i in types]
m = counts.index(max(counts))
print(types[m])
