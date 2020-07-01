import sys
import math
import string
import re
from functools import *
from itertools import *
from operator import *
# Composition related.
def comp(*funcs):
	comp2 = lambda f, g: lambda *x: f(g(*x))
	return reduce(comp2, funcs)
tuplefy = lambda f: lambda args: f(*args)
untuplefy = lambda f: lambda *args: f(args)
def curry(n, f):
	def wrap(*args):
		if n > len(args):
			return curry(n - len(args), lambda *largs: f(*args, *largs))
		return f(*args)
	return wrap
curried = curry(2, curry)
const = lambda val: lambda _: val
# Utilities
map_maybe = lambda *args: filter(partial(ne, None), map(*args))
concat_ = partial(reduce, concat)
alpha = "abcdefghijklmnopqrstuvwxyz"
fbool = comp(str.lower, str)
rbool = partial(eq, "true")
lmap = comp(list, map)
lfilter = comp(list, filter)
lrange = comp(list, range)
lreversed = comp(list, reversed)
lenumerate = comp(list, enumerate)
lmap_maybe = comp(list, map_maybe)

for _ in range(int(input())):
	y, x = map(int, input().split(" "))
	matrix = lmap(lambda _: [10] * 20, range(20))
	for row in range(20):
		for col in range(20):
			row_diff = abs(y - row)
			col_diff = abs(x - col)
			if row_diff == 0 and col_diff == 0:
				matrix[row][col] = 100
			elif row_diff <= 1 and col_diff <= 1:
				matrix[row][col] = 50
			elif row_diff <= 2 and col_diff <= 2:
				matrix[row][col] = 25
	print("\n".join(lmap(lambda row: " ".join(lmap(str, row)), matrix)))