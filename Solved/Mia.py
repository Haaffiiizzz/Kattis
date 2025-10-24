curr = input().strip()

while curr != "0 0 0 0":
    one = max(curr[0],curr[2]) + min(curr[0],curr[2])
    two = max(curr[4],curr[6]) + min(curr[4],curr[6])

    if one == two:
        print("Tie.")

    elif one == "12" or one == "21":
        if two == "12" or two == "21":
            print("Tie")
        else:
            print("Player 1 wins.")
    elif two == "12" or two == "21":
        if one == "12" or one == "21":
            print("Tie")
        else:
            print("Player 2 wins.")
    
    elif one[0] == one[1] or two[0] == two[1]:
        if two[0] != two[1]:
            print("Player 1 wins.")
        elif one[0] != one[1]:
            print("Player 2 wins.")
        elif int(one) > int(two):
            print("Player 1 wins.")
        else:
            print("Player 2 wins.")

    elif int(one) > int(two):
        print("Player 1 wins.")
    else:
        print("Player 2 wins.")
    curr = input().strip()