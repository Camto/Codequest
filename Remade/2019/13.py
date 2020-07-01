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
	rows, cols, bombs = map(int, input().split(" "))
	locs = lmap(lambda _: tuple(map(comp(partial(add, 1), int), input().split(" "))), range(bombs))
	board = lmap(lambda _: [0] * (cols + 2), range(rows + 2))
	
	for (row, col) in locs:
		for offy in range(-1, 2):
			for offx in range(-1, 2):
				board[row + offy][col + offx] += 1
	
	buf = lmap(tuplefy(lambda r, row: lmap(tuplefy(lambda c, n: str(n) if (r, c) not in locs else "*"), lenumerate(row)[1:-1])), lenumerate(board)[1:-1])
	
	print("\n".join(map(concat_, buf)))