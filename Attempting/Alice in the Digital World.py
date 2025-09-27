numData = int(input())

for _ in range(numData):
    n, m = map(int, input().split())
    numList = list(map(int, input().split()))
    maxWeight = 0

    for idx, value in enumerate(numList):
        if value == m:
            currSum = value
            left = right = idx

            while left > 0 and numList[left - 1] > m:
                currSum += numList[left - 1]
                left -= 1

            while right < n - 1 and numList[right + 1] > m:
                currSum += numList[right + 1]
                right += 1

            maxWeight = max(maxWeight, currSum)

    print(maxWeight)


numData = int(input())

# for _ in range(numData):
#     n, m = map(int, input().split())
#     numList = list(map(int, input().split()))
#     maxWeight = 0

#     for i in range(n):
#         for j in range(i+1, n):
#             sub = numList[i:j+1]
#             if min(sub) == m and sub.count(m) == 1:
#                 maxWeight = max(maxWeight, sum(sub))
#     print(maxWeight)