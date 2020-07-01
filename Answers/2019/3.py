import sys
import math
import string

cases = int(sys.stdin.readline().replace("\n", ""))

for caseNum in range(cases):
    bools = sys.stdin.readline().replace("\n", "")
    (bool1, bool2) = bools.split(" ")
    bool1 = bool1 == "true"
    bool2 = bool2 == "true"
    if bool1 == bool2:
        print("true")
    else:
        print("false")
