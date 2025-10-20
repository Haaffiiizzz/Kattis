n, l = map(int, input().split())
questions = [int(input()) for _ in range(n)]
questions.sort()
count = 0
total = 0
l = (5 * l)
i = 0

for i in range(n):
    if total + questions[i+1] <= l:
        total += questions[i]
        count += 1
    else:
        break

# while total + questions[i+1] < l and i < n:
#     total += questions[i]
#     i += 1
#     count += 1
print(count)

     