house = list(map(int,input().split()))
trees = list(map(int,input().split()))
total = list(map(int,input().split()))
apples = list(map(int,input().split()))
oranges = list(map(int,input().split()))
start = house [0]
end = house[1]
treeA = trees[0]
treeO = trees[1]
appletotal = total[0]
orangetotal = total[1]
apple = 0
orange = 0
answerA = 0
answerO = 0
for i in range(appletotal) :
    apple = treeA + apples[i]
    if apple >= start and apple <= end:
        answerA += 1
print(answerA)
for j in range(orangetotal) :
    orange = treeO + oranges[j]
    if orange <= end and orange >= start:
        answerO += 1
print(answerO)