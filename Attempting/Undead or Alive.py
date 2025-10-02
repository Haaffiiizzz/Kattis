string = input()

hasSmile = False
hasFrown = False

i = 0
while i < len(string) - 1:
    if string[i] == ":":
        if string[i+1] == "(":
            hasFrown = True
            
        elif string[i+1] == ")":
            hasSmile = True
        
    i += 1
    if hasSmile and hasFrown:
        break

if hasFrown and hasSmile:
    print("double agent")
elif hasSmile:
    print("alive")
elif hasFrown:
    print("undead")
else:
    print("machine")