import sys
import math
import string

cases = int(sys.stdin.readline().replace("\n", ""))

for caseNum in range(cases):
    given = sys.stdin.readline().replace("\n", "")
    (speed, bday) = given.split(" ")
    speed = int(speed)
    bday = bday == "true"
    if bday:
        speed -= 5
    if speed <= 60:
        print("no ticket")
    elif speed <= 80:
        print("small ticket")
    else:
        print("big ticket")
