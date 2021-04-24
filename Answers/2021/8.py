import math

for _ in range(int(input())):
  total = 0
  for _ in range(int(input().split()[0])):
    matrix_row = [int(n) for n in input().split()]
    for number in matrix_row:
      total += abs(number)**2
  n = str(round(math.sqrt(total) * 100))
  print(f"{n[:-2]}.{n[-2:]}")