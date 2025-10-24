n = int(input())
word = input().strip()

for i in range(n, 0, -1):
    if i > 1:
        print(f"{i} bottles of {word} on the wall, {i} bottles of {word}.")
        if i - 1 == 1:
            print(f"Take one down, pass it around, 1 bottle of {word} on the wall.")
        else:
            print(f"Take one down, pass it around, {i-1} bottles of {word} on the wall.")
        print()
    else:
        print(f"1 bottle of {word} on the wall, 1 bottle of {word}.")
        print(f"Take it down, pass it around, no more bottles of {word}.")
