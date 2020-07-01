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
get_list_len = lambda t, l: lmap(
	lambda _: get_in(t),
	range(l))
def get_in(expect_type):
	if expect_type in [int, float, str]:
		return expect_type(input())
	elif expect_type is bool:
		return rbool(input())
	elif type(expect_type) is tuple:
		inp = input().split(" ")
		return tuple(map(
			tuplefy(lambda t, i:
				t(i)
					if type(t) is not list
					else get_list_len(t[0], int(i))),
			zip(expect_type, inp)))
	elif type(expect_type) is list:
		return get_list_len(expect_type[0], get_in(int))

for _ in range(int(input())):