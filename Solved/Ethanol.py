num = int(input())

top = ["H"] * num
topString = "  " + " ".join(top)

second = ["|"] * num
secondString = "  " + " ".join(second)

third = ["H"] + (["C"] * num) + ["OH"]
thirdString = "-".join(third)

fourth = ["|"] * num
fourthString = "  " + " ".join(second)

bottom = ["H"] * num
bottomString = "  " + " ".join(top)

print(topString)
print(secondString)
print(thirdString)
print(fourthString)
print(bottomString)
