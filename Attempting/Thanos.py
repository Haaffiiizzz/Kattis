n = int(input())
for _ in range(n):
    data = list(map(int, input().split()))
    p = data[0]
    r = data[1]
    f = data[2]
    years = 0
    while f >= p:
        years += 1
        p = int(r*p)
    print(years)