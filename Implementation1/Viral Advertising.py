days = int(input())
x = 5
likes = 0
for _ in range(days):
    liked = int(x/2)
    likes += liked
    x = liked * 3
print(likes)
