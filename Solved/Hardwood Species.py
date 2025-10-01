import sys
from collections import Counter

speciesList = [line.strip() for line in sys.stdin if line.strip()]
totalCount = len(speciesList)

speciesCounter = Counter(speciesList)

for name in sorted(speciesCounter):
    percentage = (speciesCounter[name] / totalCount) * 100
    print(f"{name} {percentage:.4f}")
