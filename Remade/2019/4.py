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
def parse_str(expect_type, s):
	if expect_type in [int, float, str]:
		return expect_type(s)
	elif expect_type is bool:
		return rbool(s)
	elif type(expect_type) is tuple:
		inp = s.split(" ")
		return tuple(map(tuplefy(parse_str), zip(expect_type, inp)))
	elif type(expect_type) is list:
		return lmap(lambda _: get_in(expect_type[0]), range(int(s)))
get_in = lambda expect_type: parse_str(expect_type, input())
## End template.

for speed, bday in get_in([(int, bool)]):
	if bday:
		speed -= 5
	if speed <= 60:
		print("no ticket")
	elif speed <= 80:
		print("small ticket")
	else:
		print("big ticket")