hill, log, head = map(float, input().split())

hill = int(round(hill * 10))
log = int(round(log * 10))
head = int(round(head * 10))

bestDist = -1
bestLog = 0
bestHead = 0

for headCount in range(hill // head + 1):
    remaining = hill - headCount * head
    logCount = remaining // log
    total = logCount * log + headCount * head

    if total > bestDist or (total == bestDist and logCount > bestLog):
        bestDist = total
        bestLog = logCount
        bestHead = headCount

print(bestLog, bestHead)
# if hill % log == 0:
#     print(int(hill // log), 0)
# else:
#     logCount = (hill // log) + 1
#     headCount = 0

#     headMax = (hill // head)

#     while headCount < headMax:
        
#         res = (logCount * log) + (headCount * head)
        
#         if res in countMap:
#             countMap[res].append((logCount, headCount))
#         else:
#             if res <= hill:
#                 countMap[res] = [(logCount, headCount)]
        
#         if ((headCount + 1) * head) + (logCount * log) > hill:
#             logCount -= 1
#         else:
#             headCount += 1

#     bestKey = sorted(countMap.keys(), reverse=True)[0]
#     bestRes = countMap[bestKey]
#     print(int(bestRes[0][0]), int(bestRes[0][1]))


