for _ in range(int(input())):
  poly1 = list(map(int, input().split()))
  poly2 = list(map(int, input().split()))

  poly3 = [0] * 1000
  for n_i, n in enumerate(poly1):
    for m_i, m in enumerate(poly2):
      poly3[n_i + m_i] += n * m

  out = []
  for l_i, l in enumerate(poly3):
    if l != 0 and l != 1:
      if l_i > 1:
        out.append(f"+{l}x^{l_i}")
      elif l_i == 1:
        out.append(f"+{l}x")
      else:
        out.append(f"+{l}")
    elif l == 1:
      if l_i > 1:
        out.append(f"+x^{l_i}")
      elif l_i == 1:
        out.append("+x")
      elif l_i == 0:
        out.append("+1")
    elif l == -1:
      if l_i > 1:
        out.append(f"-x^{l_i}")
      elif l_i == 1:
        out.append("-x")
      elif l_i == 0:
        out.append("-1")
  out[0] = out[0][1:]
  print("".join(out))