q = int(input())
for _ in range(q):
    n = int(input())
    matrix = []
    balls = []
    containers = []

    for i in range(n):
        row = list(map(int,input().split()))
        matrix.append(row)
        containers.append(sum(row))
    balls = [sum(x) for x in zip(*matrix)]

    if sorted(balls) == sorted(containers):
        print("Possible")
    else:
        print("Impossible")

