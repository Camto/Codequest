import sys
import math
import string

cases = int(sys.stdin.readline().replace("\n", ""))

alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", 'm','n','o','p','q','r','s','t','u','v','w','x','y','z']

for caseNum in range(cases):
    shift = int(sys.stdin.readline().replace("\n", ""))
    words = sys.stdin.readline().replace("\n", "")
    print("".join(map(lambda l: alpha[(alpha.index(l) - shift) % 26] if l != " " else " ", list(words))))
