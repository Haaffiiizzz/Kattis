numTeams, numGames = map(int, input().split())

rankList = ["T" + str(i) for i in range(1, numTeams+1)]

for i in range(numGames):
    win, lost = input().split()
    if rankList.index(win) > rankList.index(lost):
        del rankList[rankList.index(lost)]
        rankList.insert(rankList.index(win) + 1, lost)

print(" ".join(rankList))