import sys


for line in sys.stdin:
    arr = list(map(int, line.split()))
    n = arr[0]
    seq = arr[1:]
    if n <= 1:
        print("Jolly")
        continue
    nums = set(range(1, n))
    for i in range(n - 1):
        diff = abs(seq[i] - seq[i + 1])
        if diff in nums:
            nums.remove(diff)
    if nums:
        print("Not jolly")
    else:
        print("Jolly")