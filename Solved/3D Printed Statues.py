n = int(input())
numPrinters = 1
count = 0
while numPrinters < n:
    numPrinters += numPrinters
    count += 1
print(count + 1)