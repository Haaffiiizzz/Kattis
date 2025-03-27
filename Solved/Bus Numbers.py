n = int(input())
busArray =  list(map(int, input().split()))
busArray = sorted(busArray)

result = []
i = 0
while i < n:
    here = [busArray[i]]
    while i < n - 1 and busArray[i + 1] - busArray[i] == 1:
        here.append(busArray[i + 1])
        i += 1
    if len(here) >= 3:
        result.append(f"{here[0]}-{here[-1]}")
    else:
        for num in here:
            result.append(str(num))
    i += 1
print(" ".join(result))

    