import string

numbers = list(map(int,input().split()))
word = str(input())
alphabets = string.ascii_lowercase
high = 0

for i in word:
    height = numbers[alphabets.index(i)]
    if height > high:
        high = height
print(high * len(word))
