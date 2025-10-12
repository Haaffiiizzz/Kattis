# r, c = map(int, input().split())
# start = tuple(map(int, input().split()))
# start = (start[0]-1, start[1]-1)
# end = tuple(map(int, input().split()))
# end = (end[0]-1, end[1]-1)
# grid = []
# for _ in range(r):
#     row = [int(ch) for ch in input().strip()]
#     grid.append(row)

# curr = start
# direc = "r"

# while curr != end:

#     if direc == "r":
#         if curr[0] > 1  and grid[curr[0] -1][curr[1]] == 0:
#             curr = (curr[0] -1, curr[1])
#             direc = "u"
#         elif curr[1] < c and grid[curr[0]][curr[1] + 1] == 0:
#             curr = (curr[0], curr[1] + 1)
            
#         elif curr[0] < r and grid[curr[0] + 1][curr[1]] == 0:
#             curr = (curr[0] + 1, curr[1])
#             direc = "d"
#         else:
#             print(0)
#             quit()
    


#     elif direc == "l":
#         if curr[0] < r and grid[curr[0] + 1][curr[1]] == 0:
#             curr = (curr[0] + 1, curr[1])
#             direc = "d"
#         elif curr[1] > 1 and grid[curr[0]][curr[1] - 1] == 0:
#             curr = (curr[0], curr[1] - 1)
#         elif curr[0] > 1 and grid[curr[0] - 1][curr[1]] == 0:
#             curr = (curr[0] - 1, curr[1])
#             direc = "u"
#         else:
#             print(0)
#             quit()

#     elif direc == "u":
#         if curr[1] > 1 and grid[curr[0]][curr[1] - 1] == 0:
#             curr = (curr[0], curr[1] - 1)
#             direc = "l"
#         elif curr[0] > 1 and grid[curr[0] - 1][curr[1]] == 0:
#             curr = (curr[0] - 1, curr[1])
#         elif curr[1] < c and grid[curr[0]][curr[1] + 1] == 0:
#             curr = (curr[0], curr[1] + 1)
#             direc = "r"
#         else:
#             print(0)
#             quit()

#     elif direc == "d":
#         if curr[1] < c and grid[curr[0]][curr[1] + 1] == 0:
#             curr = (curr[0], curr[1] + 1)
#             direc = "r"
#         elif curr[0] < r and grid[curr[0] + 1][curr[1]] == 0:
#             curr = (curr[0] + 1, curr[1])
#         elif curr[1] > 1 and grid[curr[0]][curr[1] - 1] == 0:
#             curr = (curr[0], curr[1] - 1)
#             direc = "l"
#         else:
#             print(0)
#             quit()


# print(1)


r, c = map(int, input().split())
start = tuple(map(int, input().split()))
start = (start[0] - 1, start[1] - 1)
end = tuple(map(int, input().split()))
end = (end[0] - 1, end[1] - 1)

grid = []
for _ in range(r):
    row = [int(ch) for ch in input().strip()]
    grid.append(row)

curr = start
direc = "r"
seen = set()

while curr != end:
    state = (curr, direc)
    if state in seen:
        print(0)
        quit()
    seen.add(state)

    moved = False  # Track if Carl moved this iteration

    if direc == "r":
        # Left = Up
        if curr[0] > 0 and grid[curr[0] - 1][curr[1]] == 0:
            curr = (curr[0] - 1, curr[1])
            direc = "u"
            moved = True
        # Forward = Right
        elif curr[1] < c - 1 and grid[curr[0]][curr[1] + 1] == 0:
            curr = (curr[0], curr[1] + 1)
            moved = True

        if not moved:
            direc = "d"  # Right turn only

    elif direc == "l":
        # Left = Down
        if curr[0] < r - 1 and grid[curr[0] + 1][curr[1]] == 0:
            curr = (curr[0] + 1, curr[1])
            direc = "d"
            moved = True
        # Forward = Left
        elif curr[1] > 0 and grid[curr[0]][curr[1] - 1] == 0:
            curr = (curr[0], curr[1] - 1)
            moved = True

        if not moved:
            direc = "u"

    elif direc == "u":
        # Left = Left
        if curr[1] > 0 and grid[curr[0]][curr[1] - 1] == 0:
            curr = (curr[0], curr[1] - 1)
            direc = "l"
            moved = True
        # Forward = Up
        elif curr[0] > 0 and grid[curr[0] - 1][curr[1]] == 0:
            curr = (curr[0] - 1, curr[1])
            moved = True

        if not moved:
            direc = "r"

    elif direc == "d":
        # Left = Right
        if curr[1] < c - 1 and grid[curr[0]][curr[1] + 1] == 0:
            curr = (curr[0], curr[1] + 1)
            direc = "r"
            moved = True
        # Forward = Down
        elif curr[0] < r - 1 and grid[curr[0] + 1][curr[1]] == 0:
            curr = (curr[0] + 1, curr[1])
            moved = True

        if not moved:
            direc = "l"

    # If he neither moved nor turned (dead end)
    if not moved and (curr, direc) in seen:
        print(0)
        quit()

print(1)
