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
	given = map_maybe(
		lambda s: None if s.strip() == "" else s.strip(),
		input().replace("and", "").replace(",", " ").split(" "))
	seconds = minutes = hours = "0"
	for time in given:
		suffix = time[-1]
		if suffix == "s":
			seconds = time[:-1]
		elif suffix == "m":
			minutes = time[:-1]
		elif suffix == "h":
			hours = time[:-1]
	print(f"{hours.zfill(2)}:{minutes.zfill(2)}:{seconds.zfill(2)}")