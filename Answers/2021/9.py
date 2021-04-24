currency = [10000, 5000, 2000, 1000, 500, 200, 100, 25, 10, 5, 1]

for _ in range(int(input())):
  money = input()
  money = int(money[:-3] + money[-2:])
  out = ""
  for c in currency:
    out += str(money // c)
    money %= c
  print(out)