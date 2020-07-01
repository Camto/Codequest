import sys
import math
import string

cases = int(sys.stdin.readline().replace("\n", ""))

for _ in range(cases):
    ns = sys.stdin.readline().replace("\n", "")
    (ds, rounds, dpr) = map(int, ns.split(" "))
    doors = list(map(lambda d: 1/ds, range(ds)))

    sbc = 0
    for _ in range(rounds):
        sbc += 1
        pretotal = sum(doors[sbc:(ds - list(map(lambda d: d != 0, reversed(doors))).index(True)) - 2])
        otr = []
        for _ in range(dpr):
            opened = (ds - list(map(lambda d: d != 0, reversed(doors))).index(True)) - 2
            doors[opened] = 0
            otr.append(opened)
        min(otr) - 1 - sbc
