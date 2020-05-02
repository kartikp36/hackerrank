nandk = list(map(int,input().split()))
nitem = nandk[0]
kitem = nandk[1]
costs = list(map(int,input().split()))
charged = int(input())
realcharge = (sum(costs) - costs[kitem])/2
if charged == realcharge :
    print("Bon Appetit")
else :
    print(int(charged-realcharge))