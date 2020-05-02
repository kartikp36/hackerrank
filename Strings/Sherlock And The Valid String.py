import sys
from collections import Counter
from statistics import mode

strings = str(input())
counts = Counter(strings)

freq = [ v for _,v in counts.items()]
nums = list(set(freq))
l = len(nums)

if l == 1:
    print("YES")
    exit()
elif l == 2:
    try:
        m = mode(freq)
        nums.remove(m)
    except:
        pass
    n = nums[0]
    if freq.count(n) == 1 and (n-1 == m or n-1 == 0):
        print("YES")
        sys.exit(0)

print("NO")
exit()
