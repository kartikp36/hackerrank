def nextPermutation(arr):
    n = len(arr)-1
    m = int(n)
    while n >= 1:
        if arr[n] > arr[n-1]:
            pivot = n-1
            while m >= n:
                if arr[m] > arr[pivot]:
                    temp = arr[pivot]
                    arr[pivot] = arr[m]
                    arr[m] = temp
                    arr[n:] = arr[:n-1:-1]
                    return arr
                m -= 1
        n -= 1
    return 'no answer'

n = int(input())
for _ in range(n):
    print(''.join(nextPermutation(list(input()))))

