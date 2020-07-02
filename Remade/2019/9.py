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

for times in get_in([str]):
	times = map_maybe(
		lambda s: None if s.strip() == "" else s.strip(),
		times.replace("and", "").replace(",", " ").split(" "))
	seconds = minutes = hours = "0"
	for time in times:
		suffix = time[-1]
		if suffix == "s":
			seconds = time[:-1]
		elif suffix == "m":
			minutes = time[:-1]
		elif suffix == "h":
			hours = time[:-1]
	print(f"{hours.zfill(2)}:{minutes.zfill(2)}:{seconds.zfill(2)}")