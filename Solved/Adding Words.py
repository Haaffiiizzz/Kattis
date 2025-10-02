from sys import stdin
defs = {}

for line in stdin:
    
    if line.startswith("def"):
        defs[line.split(" ")[1]] = int(line.split(" ")[2])
        
    elif line.startswith("clear"):
        defs = {}
        defsNum = {}
        
    elif line.startswith("calc"):
        original = line[5:-1]
        #cont here
        result = defs.get(line.split(" ")[1], "unknown")
        i = 2
        line = line.split(" ")
        
        while i < len(line) - 2 and result != "unknown":
            if line[i] == "+":
                number = defs.get(line[i+1], None)
                if number != None:
                    result += number
                else:
                    result = "unknown"
            elif line[i] == "-":
                number = defs.get(line[i+1], None)
                if number != None:
                    result -= number
                else:
                    result = "unknown"
            i += 2
            
        for key, value in defs.items():
            if value == result:
                result = key
                break
        
        if result == "unknown" or type(result) == int:
            print(f"{original} unknown")
        else:
            print(f"{original} {result}")