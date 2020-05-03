x = int(input())
y = int(input())
kaprekarFound = False
for i in range(x,y+1):
    d = len(str(i))
    sq = str(i*i)
    split = len(sq) - d
    r = sq[split:]
    l = sq[:split]
    if l == "" :
        l = 0
    if int(r)  + int(l) == i:
        print(i,end=" ")
        kaprekarFound = True
if not kaprekarFound:
    print("INVALID RANGE")
