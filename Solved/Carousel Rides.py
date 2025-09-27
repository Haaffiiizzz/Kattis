n, m = map(int, input().split())

while n != 0 and m != 0:

    numOffers = n
    bestoffer = float("inf")
    bestTup = (0, float("inf"))
    for i in range(n):
        a, b = map(int, input().split())

        if a > m:
            continue
        each = b / a

        if each < bestoffer:
            bestoffer = each
            bestTup = (a, b)
        elif each == bestoffer:
            if a > bestTup[0]:
                bestoffer = each
                bestTup = (a, b)
        
    if bestTup[0] == 0:
        print("No suitable tickets offered")
    else:
        print(f"Buy {bestTup[0]} tickets for ${bestTup[1]}")
    n, m = map(int, input().split())

