# sentence = input().split()

# n = len(sentence)
# Map = {}

# i = 0

# while i < n:

#     curr = sentence[i]
#     count = 1
#     while i < n - 1 and sentence[i] == sentence[i+1]:
#         # consecMap[curr] = min(consecMap.get(curr, 80), i)
#         i += 1
#         count += 1
#     if curr in Map:
#         Map[curr] = max(Map[curr], count)
#     else:
#         Map[curr] = count
#     i += 1


# res = sorted(Map.keys(), reverse= True, key = lambda x: Map[x])

# biggest = res[0]
# print(biggest)

sentence = input().split()
n = len(sentence)

i = 0
bestWord = ""
bestCount = 0

while i < n:
    curr = sentence[i]
    count = 1

    while i + 1 < n and sentence[i+1] == curr:
        count += 1
        i += 1
    if bestCount < count:
        bestCount = count
        bestWord = curr

    i += 1
print(bestWord)