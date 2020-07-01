# Basic imports.
import sys
import math
import string
import re

# Functional imports.
from functools import *
from itertools import *
from operator import *

# Function composition.
def comp(*funcs):
	comp2 = lambda f, g: lambda *x: f(g(*x))
	return reduce(comp2, funcs)

# To compose multiargument functions easier.
tuplefy = lambda f: lambda args: f(*args)
untuplefy = lambda f: lambda *args: f(args)

# Function currying.
def curry(n, f):
	def wrap(*args):
		if n > len(args):
			return curry(n - len(args), lambda *largs: f(*args, *largs))
		return f(*args)
	return wrap
	
# Curry as a decorator.
curried = curry(2, curry)

# The constant function.
const = lambda val: lambda _: val

# Map and filter combined.
map_maybe = lambda *args: filter(partial(ne, None), map(*args))

# Haskell-like concat.
concat_ = partial(reduce, concat)

# The alphabet.
alpha = "abcdefghijklmnopqrstuvwxyz"

# Bool formatting and reading.
fbool = comp(str.lower, str)
rbool = partial(eq, "true")

# Shorter list conversion.
lmap = comp(list, map)
lfilter = comp(list, filter)
lrange = comp(list, range)
lreversed = comp(list, reversed)
lenumerate = comp(list, enumerate)
lmap_maybe = comp(list, map_maybe)

# Parse all the problem's input at once.

parse_list = lambda t, l: lmap(
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
					else parse_list(t[0], int(i))),
			zip(expect_type, inp)))
	elif type(expect_type) is list:
		return parse_list(expect_type[0], get_in(int))