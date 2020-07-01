import sys
import math
import string

cases = int(sys.stdin.readline().replace("\n", ""))

for caseNum in range(cases):
    given = sys.stdin.readline().replace("\n", "")
    given = list(filter(lambda s: s != "", map(lambda s: s.strip(), given.replace("and", "").replace(",", " ").split(" "))))
    seconds = 0
    minutes = 0
    hours = 0
    for time in given:
        thing = time[-1]
        if thing == "s":
            seconds += int(time[:-1])
        elif thing == "m":
            minutes += int(time[:-1])
        elif thing == "h":
            hours += int(time[:-1])
    print(f"{hours:2}:{minutes:2}:{seconds:2}".replace(" ", "0"))
