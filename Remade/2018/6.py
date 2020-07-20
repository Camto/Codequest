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

for inp in get_in(["[^ ]+"]):
	bools = lmap(lambda s: s == "WORKING", inp)
	n = sum(map(tuplefy(lambda i, n: 0 if bools[i] else n), lenumerate([8, 4, 2, 1])))
	
	topnum = n // 4
	if topnum == 0: light1 = "off"
	elif topnum == 1: light1 = "red"
	elif topnum == 2: light1 = "green"
	else: light1 = "blue"
	
	bottomnum = n % 4
	if bottomnum == 0: light2 = "off"
	elif bottomnum == 1: light2 = "red"
	elif bottomnum == 2: light2 = "green"
	else: light2 = "blue"
	
	print(light1, light2)