nums = list(input().split())
lastDig = nums[-1][-1]
if lastDig == "0":
    print(10)
else:
    print(lastDig)