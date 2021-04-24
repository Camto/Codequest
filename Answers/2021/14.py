import string

left = 0
right = 1

def dir_to_sign(dir):
  if dir == left:
    return 1
  elif dir == right:
    return -1

for _ in range(int(input())):
  text = input()
  shift_vals = [int(n) for n in input().split()]
  shift_dirs = [int(n) for n in input().split()]
  out = ""
  val_idx = 0
  dir_idx = 0
  for c in text:
    if c in string.ascii_uppercase:
      n = ord(c) - 65
      n += dir_to_sign(shift_dirs[dir_idx]) * shift_vals[val_idx]
      out += chr((n % 26) + 97)
      val_idx += 1
      dir_idx += 1
      val_idx %= len(shift_vals)
      dir_idx %= len(shift_dirs)
    else:
      out += c
  print(out)