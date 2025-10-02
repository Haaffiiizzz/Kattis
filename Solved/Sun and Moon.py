sunAgo, sunYears = map(int, input().split())
moonAgo, moonYears = map(int, input().split())


sunNext = sunAgo + 1
moonNext = moonAgo + 1
i = 1
while True:
    sunNext = (sunNext % sunYears) + 1
    moonNext = (moonNext % moonYears) + 1
    big = max(sunNext, moonNext)
    small = min(sunNext, moonNext)

    if big % small == 0:
        break
    i += 1
print(i)