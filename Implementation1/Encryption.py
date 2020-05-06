from math import sqrt,ceil,floor

string = str(input())
s = string.replace(" ", "")
length = len(s)
l = sqrt(length)
row = floor(l)
column = ceil(l)
if row * column < length:
    row += 1

answer = ""
matrix = []

for _ in range(row):
    matrix.append(list(s[:column]))
    s = s[column:]

for c in range(column):
    for r in range(row):
        try:
            answer += matrix[r][c]
        except:
            pass
    answer += " "
print(answer)
