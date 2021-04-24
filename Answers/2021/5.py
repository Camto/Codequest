for _ in range (int(input())):
  asteroids = {}
  for __ in range (int(input())):
    x, y = [int(n) for n in input().split()]
    dist = x**2 + y**2
    asteroids[dist] = (x, y)
  for k in sorted(asteroids):
    x, y = asteroids[k]
    print(x, y)