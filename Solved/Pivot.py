n = int(input())
array = [int(x) for x in input().split()]
count = 0

leftMax = [0] * n
leftMax[0] = array[0]

for i in range(1, n):
    leftMax[i] = max(leftMax[i-1], array[i])
    
rightMin = [0] * n
rightMin[-1] = array[-1]

for i in range(n-2, -1, -1):
    rightMin[i] = min(rightMin[i+1], array[i])
    
for i in range(n):
    if (i == 0 or array[i] >= leftMax[i-1]) and (i== n-1 or array[i] <= rightMin[i + 1]):
        count += 1
print(count)