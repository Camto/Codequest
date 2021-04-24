for _ in range(int(input())):
  inp = input().split()
  format = inp.pop(0)
  if format == "formatHeight":
    print(f"{inp[0]}'{inp[1]}\"")
  elif format == "formatDate":
    print(f"{inp[0].zfill(4)}{inp[1].zfill(2)}{inp[2].zfill(2)}")
  elif format == "concatenate":
    print(",".join(inp))