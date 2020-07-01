import sys
import math
import string

cases = int(sys.stdin.readline().replace("\n", ""))

def fb(ls):
    return "".join(list(map(lambda b: "1" if b else "0", list(reversed(ls)))))

for caseNum in range(cases):
    n = int(sys.stdin.readline().replace("\n", ""))
    buf = list(map(lambda _: False, list(range(n))))
    print(fb(buf))
    for _ in range(2**n - 1):
        carry = buf[0]
        buf[0] = not buf[0]
        for i in range(1, len(buf)):
            if carry:
                carry = buf[i]
                buf[i] = not buf[i]
        print(fb(buf))
