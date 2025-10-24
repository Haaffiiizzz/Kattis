n = int(input())
nums = list(map(int, input().split()))

# Sort and merge using a stack: whenever the top two are equal, combine.
nums.sort()
stack = []
for x in nums:
    stack.append(x)
    while len(stack) >= 2 and stack[-1] == stack[-2]:
        v = stack.pop()
        stack[-1] = v * 2

print(len(stack))

