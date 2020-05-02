queries = int(input())
for i in range(queries) :
    mix = list(map(int,input().split()))
    catA = mix[0]
    catB = mix[1]
    mouse = mix[2]
    if abs(catA - mouse) == abs(catB - mouse) :
        print("Mouse C")
    elif abs(catA - mouse) < abs(catB - mouse) :
        print("Cat A")
    if abs(catA - mouse) > abs(catB - mouse) :
        print("Cat B")