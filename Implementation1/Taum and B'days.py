t = int(input())
for _ in range(t):
    gifts = list(map(int,input().split()))
    costs = list(map(int,input().split()))
    b = gifts[0]
    w = gifts[1]
    bc = costs[0]
    wc = costs[1]
    z = costs[2]
    if z < abs(bc - wc):
        if bc > wc + z:
            bc = wc + z
        if wc > bc + z:
            wc = bc + z
    print(b*bc + w*wc)
