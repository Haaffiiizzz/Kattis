a, b, c = map(int, input().split())

operators = ['+', '-', '*', '/']
results = []

for op1 in operators:
    for op2 in operators:
        try:
            if op1 == '+':
                temp = a + b
            elif op1 == '-':
                temp = a - b
            elif op1 == '*':
                temp = a * b
            elif op1 == '/':
                if b == 0 or a % b != 0:
                    continue
                temp = a // b

            if op2 == '+':
                val = temp + c
            elif op2 == '-':
                val = temp - c
            elif op2 == '*':
                val = temp * c
            elif op2 == '/':
                if c == 0 or temp % c != 0:
                    continue
                val = temp // c

            if val >= 0:
                results.append(val)
        except:
            continue

print(min(results))