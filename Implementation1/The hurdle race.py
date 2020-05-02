mix = list(map(int,input().split()))
total = mix[0]
maximum = mix[1]
hurdles = list(map(int,input().split()))
if max(hurdles) >= maximum:
    print(max(hurdles)-maximum)
else :
    print("0")