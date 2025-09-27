asciiArtMap = {
    '0': [
        "xxxxx",
        "x...x",
        "x...x",
        "x...x",
        "x...x",
        "x...x",
        "xxxxx"
    ],
    '1': [
        "....x",
        "....x",
        "....x",
        "....x",
        "....x",
        "....x",
        "....x"
    ],
    '2': [
        "xxxxx",
        "....x",
        "....x",
        "xxxxx",
        "x....",
        "x....",
        "xxxxx"
    ],
    '3': [
        "xxxxx",
        "....x",
        "....x",
        "xxxxx",
        "....x",
        "....x",
        "xxxxx"
    ],
    '4': [
        "x...x",
        "x...x",
        "x...x",
        "xxxxx",
        "....x",
        "....x",
        "....x"
    ],
    '5': [
        "xxxxx",
        "x....",
        "x....",
        "xxxxx",
        "....x",
        "....x",
        "xxxxx"
    ],
    '6': [
        "xxxxx",
        "x....",
        "x....",
        "xxxxx",
        "x...x",
        "x...x",
        "xxxxx"
    ],
    '7': [
        "xxxxx",
        "....x",
        "....x",
        "....x",
        "....x",
        "....x",
        "....x"
    ],
    '8': [
        "xxxxx",
        "x...x",
        "x...x",
        "xxxxx",
        "x...x",
        "x...x",
        "xxxxx"
    ],
    '9': [
        "xxxxx",
        "x...x",
        "x...x",
        "xxxxx",
        "....x",
        "....x",
        "xxxxx"
    ],
    '+': [
        ".....",
        "..x..",
        "..x..",
        "xxxxx",
        "..x..",
        "..x..",
        "....."
    ]
}

height = 7
lines = [input() for _ in range(height)]
width = len(lines[0])

charWidth = 5
sepWidth = 1

numChars = (width + 1) // (charWidth + sepWidth)

charBlocks = []
for i in range(numChars):
    startCol = i * (charWidth + sepWidth)
    charBlock = [line[startCol:startCol + charWidth] for line in lines]
    charBlocks.append(charBlock)

def identifyChar(block):
    for key, value in asciiArtMap.items():
        if block == value:
            return key

expressionChars = [identifyChar(block) for block in charBlocks]
expression = ''.join(expressionChars)

leftStr, rightStr = expression.split('+')
result = str(int(leftStr) + int(rightStr))


outputLines = ['' for _ in range(height)]
for idx, digit in enumerate(result):
    digitArt = asciiArtMap[digit]
    for row in range(height):
        outputLines[row] += digitArt[row]
    if idx != len(result) - 1:
        for row in range(height):
            outputLines[row] += '.'

for line in outputLines:
    print(line)
