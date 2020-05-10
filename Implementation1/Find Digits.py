cases = int(input())

for _ in range(cases):
    count = 0
    number = int(input())
    num = str(number)
    digits = list(set(num.replace("0","")))
    for n in digits:
        if number % int(n) == 0:
            count += num.count(n)
    print(count)
