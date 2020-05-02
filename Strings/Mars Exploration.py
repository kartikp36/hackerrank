message = list(input())
answer = 0
number = int(len(message)/3)
for i in range(0,number) :
    i = i*3
    if message[i] != "S":
        answer += 1
    if message[i+1] != "O":
        answer += 1
    if message[i+2] != "S":
        answer += 1
print(answer)