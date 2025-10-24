n = int(input())

for _ in range(n):
    Dict = {}
    strings = input().split()
    for s in strings:
        if s in Dict:
            Dict[s] += 1
        else:
            Dict[s] = 1
    biggest = max(Dict.keys(), key = lambda x: Dict[x])

    if biggest == "1":
        print("leader")
    elif biggest == "2":
        print("intellectual")
    elif biggest == "3":
        print("social")
    else:
        print("practical")
    