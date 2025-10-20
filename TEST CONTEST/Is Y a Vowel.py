string = input()

vowels = {"a": 1, "e": 1, "i":1, "o": 1, "u": 1}
vowelCount = 0
ycount = 0

for i in string:
    if vowels.get(i):
        vowelCount += 1
    elif i == "y":
        ycount += 1

print(vowelCount, vowelCount + ycount)