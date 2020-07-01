import sys
import math
import string

cases = int(sys.stdin.readline().replace("\n", ""))

for _ in range(cases):
    ns = sys.stdin.readline().replace("\n", "")
    (rows, cols, bombs) = map(int, ns.split(" "))

    locs = []
    for _ in range(bombs):
        ns = sys.stdin.readline().replace("\n", "")
        (x, y) = map(int, ns.split(" "))
        locs.append((x, y))

    board = list(map(lambda _: list(range(cols + 2)), list(range(rows + 2))))

    for row in range(rows + 2):
        for col in range(cols + 2):
            board[row][col] = 0
    
    for row in range(rows + 2):
        for col in range(cols + 2):
            if (row - 1, col - 1) in locs:
                for (offx, offy) in [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]:
                    board[row + offy][col + offx] += 1

    buf = ""
    
    for row in range(rows):
        for col in range(cols):
            if (row, col) in locs:
                buf += "*"
            else:
                buf += str(board[row + 1][col + 1])
        buf += "\n"

    print(buf)
