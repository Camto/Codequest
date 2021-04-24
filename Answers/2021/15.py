import math

for _ in range(int(input())):
  valid_times = []
  for __ in range(int(input())):
    day, ti, thick, wspeed, wdirection = input().split()
    thick = int(thick)
    wspeed= float(wspeed)
    wdirection= int(wdirection)
    wdns= abs(math.cos(wdirection / 180 * math.pi)*wspeed)
    wdew= abs(math.sin(wdirection / 180 * math.pi)*wspeed)
    if thick > 1000:
      pass
    elif wdns > 20:
      pass
    elif wdew > 40:
      pass
    else:
      valid_times.append((day, ti))
  if len(valid_times) > 0:
    print(" ".join(valid_times[0]))
  else:
    print("ABORT LAUNCH")