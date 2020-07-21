## Begin template https://github.com/Camto/Codequest .
import sys; import math; import string; import re
from functools import *; from itertools import *; from operator import *
## Composition related.
comp = lambda *funcs: reduce(lambda f, g: lambda *x: f(g(*x)), funcs)
tuplefy = lambda f: lambda args: f(*args); untuplefy = lambda f: lambda *args: f(args)
## Utility functions.
map_maybe = lambda *args: filter(partial(ne, None), map(*args))
fbool = comp(str.lower, str); rbool = partial(eq, "true")
matrix = lambda cols, rows, val: lmap(lambda _: [val] * cols, range(rows))
chunks = lambda l, n: [l[i * n:(i + 1) * n] for i in range((len(l) + n - 1) // n)]
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
	elif type(expect_type) is str:
		return re.findall(expect_type, s)
	elif type(expect_type) is tuple:
		return (parse_str(s, expect_type[0]),) + tuple(map(get_in, expect_type[1:]))
	elif type(expect_type) is list:
		return lmap(lambda _: parse_str(input(), *expect_type), range(int(s)))
get_in = lambda *expect_types: parse_str(input(), *expect_types)
## End template.

for [strs] in get_in(["(\d+),(\d+)"]):
	n1, n2 = map(int, strs)
	minuend = max(n1, n2)
	subtrahend = min(n1, n2)
	diff = minuend - subtrahend
	
	while diff != 0:
		print(f"{minuend}-{subtrahend}={diff}")
		minuend = max(subtrahend, diff)
		subtrahend = min(subtrahend, diff)
		diff = minuend - subtrahend
	print(f"{minuend}-{subtrahend}={diff}")
	
	if minuend == 1: print("COPRIME")
	else: print("NOT COPRIME")