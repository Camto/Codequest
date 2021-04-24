import string

for _ in range(int(input())):
  text = "".join([input().upper() for _ in range(int(input()))])
  freq = {}
  tot = 0
  for l in string.ascii_uppercase:
    freq[l] = text.count(l)
    tot += freq[l]
  
  for l in string.ascii_uppercase:
    s = str(round(freq[l]/tot * 10000)).zfill(3)
    print(f"{l}: {s[:-2]}.{s[-2:]}%")