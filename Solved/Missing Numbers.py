n = int(input())
recited = [int(input()) for _ in range(n)]
done = True
for i in range(1, recited[-1]+1):
    if i not in recited:
        done = False
        print(i)

if done:
    print("good job")