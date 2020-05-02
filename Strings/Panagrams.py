string = sorted(set(input()))
alphabets =[97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122]
ASCII = []
answer = 0
notlowercase = []
for i in string :
    ASCII.append(ord(i))
for a in alphabets :
    if a in ASCII :
        answer += 1
    else:
        notlowercase.append(a)
for n in notlowercase:
    if (n-32) in ASCII:
        answer += 1
if answer == 26 :
    print("pangram")
else :
    print("not pangram")