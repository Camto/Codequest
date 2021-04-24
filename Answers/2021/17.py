for _ in range(int(input())):
  matrix = [input().split(",") for _ in range(int(input().split()[0]))]
  print("\n".join([",".join(row) for row in zip(*matrix)]))