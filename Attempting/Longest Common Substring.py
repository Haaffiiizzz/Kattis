n = int(input())

words = [input() for _ in range(n)]

least = len(min(words, key=len))

i = 0

while i < least:

    j = 0

    while j < least:
        
        for word in words:
            