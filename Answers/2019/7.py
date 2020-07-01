import sys
import math
import string

cases = int(sys.stdin.readline().replace("\n", ""))

for _ in range(cases):
    subcases = int(sys.stdin.readline().replace("\n", ""))
    numbers = []
    for _ in range(subcases):
        numbers.append(float(sys.stdin.readline().replace("\n", "")))
    minimum = min(numbers)
    maximum = max(numbers)
    for n in numbers:
        print(round(255 * (n - minimum) / (maximum - minimum)))
