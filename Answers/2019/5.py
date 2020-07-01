import sys
import math
import string

cases = int(sys.stdin.readline().replace("\n", ""))

for caseNum in range(cases):
    given = sys.stdin.readline().replace("\n", "")
    (n1, n2, n3) = list(map(int, given.split(" ")))
    n3 -= min(n2, n3 // 5) * 5 # Use long bricks.
    print(str(n1 >= n3).lower())
