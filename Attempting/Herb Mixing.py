g, r = map(int, input().split())

total = 0

while g > 0:
    if g <= r:
        total += g * 10
        break
    total  