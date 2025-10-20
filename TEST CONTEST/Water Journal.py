n, a, b = map(int, input().split())

drinks = [int(input()) for _ in range(n-1)]

minDrink = min(drinks)
maxDrink = max(drinks)

if minDrink == a and maxDrink == b:
    for i in range(a, b+1):
        print(i)
elif minDrink == a:

    print(b)
elif maxDrink == b:
    print(a)

else:
    print(-1)
#possible if a == b