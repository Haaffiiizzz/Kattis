Dict = dict()

name = input()

while name != "***":
    if name in Dict:
        Dict[name] += 1
    else:
        Dict[name] = 1
    name = input()
    
resultList = list(Dict.keys())
resultList.sort(key= lambda x: [Dict[x]], reverse=True)

if Dict[resultList[0]] == Dict[resultList[1]]:
    print("Runoff!")
else:
    print(resultList[0])