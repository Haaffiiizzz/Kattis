import ast
from collections import deque

testCases = int(input())

for _ in range(testCases):
    program = input().strip()
    numCount = int(input())
    rawInput = input().strip()
    numDeque = deque(ast.literal_eval(rawInput))

    isReversed = False
    hasError = False

    for command in program:
        if command == "R":
            isReversed = not isReversed
        else:
            if not numDeque:
                print("error")
                hasError = True
                break
            if isReversed:
                numDeque.pop()
            else:
                numDeque.popleft()

    if not hasError:
        if isReversed:
            numDeque.reverse()
        print("[" + ",".join(map(str, numDeque)) + "]")
