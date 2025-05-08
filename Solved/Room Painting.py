INPUT = input().split()
n = int(INPUT[0])
m = int(INPUT[1])
waste = 0

sizes = [int(input()) for _ in range(n)]
needed = [int(input()) for _ in range(m)]

sizes = sorted(sizes)
needed = sorted(needed)

i = 0
j = 0

while i < m:
    if sizes[j] < needed[i]:
        j += 1
    else:
        waste += sizes[j] - needed[i]
        i += 1
    
print(waste)