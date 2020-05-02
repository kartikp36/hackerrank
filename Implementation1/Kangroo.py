mix = list(map(int,input().split()))
position1 = mix[0]
speed1 = mix[1]
position2 = mix[2]
speed2 = mix[3]
answer ="NO"
kangroo1 = position1
kangroo2 = position2
for _ in range(100):
    kangroo1 = kangroo1 + speed1 
    kangroo2 = kangroo2 + speed2
    if kangroo1 == kangroo2 :
       answer = "YES"
print(answer)