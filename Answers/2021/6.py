import string

# string.ascii_lowercase.index('a') + 1
for _ in range (int(input())):
  word = input()
  tot = 0
  for letter in word:
    tot += string.ascii_lowercase.index(letter) + 1
  print(tot)