n = int(input())

stuff = [input().split() for _ in range(n)]

k = int(input())
c = 0
g = 0

for s in stuff:
    if int(s[1]) < k:
        if s[0] == "CAUGHT":
            c += int(s[2])
            g += int(s[3])
        else:
            c -= int(s[2])
            g -= int(s[3])

print(c, g)