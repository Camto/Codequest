## Begin template.
import sys
import math
import string
import re
from functools import *
from itertools import *
from operator import *
## Composition related.
def comp(*funcs):
	comp2 = lambda f, g: lambda *x: f(g(*x))
	return reduce(comp2, funcs)
tuplefy = lambda f: lambda args: f(*args)
untuplefy = lambda f: lambda *args: f(args)
## Utility functions.
map_maybe = lambda *args: filter(partial(ne, None), map(*args))
alpha = "abcdefghijklmnopqrstuvwxyz"
fbool = comp(str.lower, str)
rbool = partial(eq, "true")
lmap = comp(list, map)
lfilter = comp(list, filter)
lrange = comp(list, range)
lreversed = comp(list, reversed)
lenumerate = comp(list, enumerate)
lmap_maybe = comp(list, map_maybe)
## Input parsing.
parse_list = lambda t, l: lmap(lambda _: get_in(t), range(l))
def get_in(expect_type):
	if expect_type in [int, float, str]:
		return expect_type(input())
	elif expect_type is bool:
		return rbool(input())
	elif type(expect_type) is tuple:
		inp = input().split(" ")
		return tuple(map(
			tuplefy(lambda t, i:
				t(i) if type(t) is not list else parse_list(t[0], int(i))),
			zip(expect_type, inp)))
	elif type(expect_type) is list:
		return parse_list(expect_type[0], get_in(int))
lmap(solution, get_in(<INPUT HERE>))

def solution(given):
## End template.