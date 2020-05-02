total = int(input())
scores = list(map(int,input().split()))
highscore = 0
lowscore = 0
for i in range(1,total):
    if scores[i] > max(scores[0:i]):
        highscore += 1
for j in range(1,total):
    if scores[j] < min(scores[0:j]):
        lowscore += 1
print(highscore,lowscore)