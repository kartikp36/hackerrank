int(input())
score = list(map(int,input().split()))
score = sorted(set(score))
n = len(score)
levels = int(input())
AliceScores = list(map(int,input().split()))
sortedScores = sorted(AliceScores)

answer = {}
j = 0
for i in sortedScores:
    if i in score:
        answer[i] = n - score.index(i)
    elif i > max(score):
        answer[i] = 1
    elif i < min(score):
        answer[i] = (n + 1)
    else:
        while i > score[j]:
            j += 1
        answer[i] = n-j+1
for i in AliceScores:
    print(answer[i])
