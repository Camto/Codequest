import sys
import math
import string

cases = int(sys.stdin.readline().replace("\n", ""))

for _ in range(cases):
    numbers = sys.stdin.readline().replace("\n", "")
    (y, x) = map(int, numbers.split(" "))

    matrix = list(map(lambda _: list(range(20)), list(range(20))))
    for row in range(20):
        for col in range(20):
            if col == x and row == y:
                matrix[row][col] = 100
            elif (col - 1 == x or col + 1 == x or col == x) and (row - 1 == y or row + 1 == y or row == y):
                matrix[row][col] = 50
            elif (x in range(col - 2, col + 3)) and (y in range(row - 2, row + 3)):
                matrix[row][col] = 25
            else:
                matrix[row][col] = 10
    print("\n".join(list(map(lambda row: " ".join(list(map(str, row))), matrix))))
