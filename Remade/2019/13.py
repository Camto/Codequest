## Begin template https://github.com/Camto/Codequest .
import sys; import math; import string; import re
from functools import *; from itertools import *; from operator import *
## Composition related.
comp = lambda *funcs: reduce(lambda f, g: lambda *x: f(g(*x)), funcs)
tuplefy = lambda f: lambda args: f(*args); untuplefy = lambda f: lambda *args: f(args)
## Utility functions.
map_maybe = lambda *args: filter(partial(ne, None), map(*args))
alpha = "abcdefghijklmnopqrstuvwxyz"
fbool = comp(str.lower, str); rbool = partial(eq, "true")
lmap = comp(list, map); lfilter = comp(list, filter); lrange = comp(list, range)
lreversed = comp(list, reversed); lenumerate = comp(list, enumerate); lmap_maybe = comp(list, map_maybe)
## Input parsing.
def parse_str(s, *expect_types):
	if len(expect_types) > 1:
		inp = s.split(" ")
		return tuple(map(tuplefy(parse_str), zip(inp, expect_types)))
	expect_type = expect_types[0]
	if expect_type in [int, float, str]:
		return expect_type(s)
	elif expect_type is bool:
		return rbool(s)
	elif type(expect_type) is tuple:
		return (parse_str(s, expect_type[0]),) + tuple(map(get_in, expect_type[1:]))
	elif type(expect_type) is list:
		return lmap(lambda _: parse_str(input(), *expect_type), range(int(s)))
get_in = lambda *expect_types: parse_str(input(), *expect_types)
## End template.

for rows, cols, locs in get_in([int, int, [int, int]]):
	locs = lmap(tuplefy(lambda x, y: (x + 1, y + 1)), locs)
	board = lmap(lambda _: [0] * (cols + 2), range(rows + 2))
	
	for (row, col) in locs:
		for offy in range(-1, 2):
			for offx in range(-1, 2):
				board[row + offy][col + offx] += 1
	
	buf = lmap(tuplefy(lambda r, row: lmap(tuplefy(lambda c, n: str(n) if (r, c) not in locs else "*"), lenumerate(row)[1:-1])), lenumerate(board)[1:-1])
	
	print("\n".join(map(partial(reduce, concat), buf)))