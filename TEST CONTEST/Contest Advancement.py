n, k , c = map(int, input().split())
teams = [tuple(input().split() + [str(i)]) for i in range(n)]
schoolLimit = {}
reserve = []
totalPrinted = 0
i = 0
result = []

while totalPrinted < k and i < n:
    team = teams[i]
    if team[1] in schoolLimit:

        if schoolLimit[team[1]] < c:
            result.append(team)
            totalPrinted += 1
            schoolLimit[team[1]] += 1
        else:
            reserve.append(team)
    
    else:
        schoolLimit[team[1]] = 1
        result.append(team)
        totalPrinted += 1
    i += 1

remaining = k - totalPrinted
if remaining > 0:
    for i in range(remaining):
        result.append(reserve[i])
    
result.sort(key= lambda x: int(x[2]))
for i in result:
    print(i[0])
