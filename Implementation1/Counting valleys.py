total = int(input())
steps = list(input())
steplevel = 0
heights = [0]
valleys = 0
for i in steps :
    if i == 'U' :
        steplevel += 1
    if i == 'D' :
        steplevel -= 1
    heights.append(steplevel)
for h in range(len(heights)-1):
    if heights[h] == 0 and heights[h+1] == -1 :
        valleys += 1
print(valleys)