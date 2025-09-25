strrr = input()

i = 0
A = 0
B = 0

while i < len(strrr):
    if strrr[i] == "A":
        A += int(strrr[i+1])
    else:
        B += int(strrr[i+1])
    
    if (A >= 11 and A - B >= 2) or (A == 11 and B < 10):
        print("A")
        quit()
    elif (B >= 11 and B - A >= 2) or (B == 11 and A < 10):
        print("B")
        quit()
    i += 2