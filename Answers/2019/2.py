import sys
import math
import string

cases = int(sys.stdin.readline().replace("\n", ""))

for caseNum in range(cases):
    ns = sys.stdin.readline().replace("\n", "")
    (n1, n2) = ns.split(" ")
    n1 = int(n1)
    n2 = int(n2)
    if n1 == n2:
        print(2 * (n1 + n2))
    else:
        print(n1 + n2)
