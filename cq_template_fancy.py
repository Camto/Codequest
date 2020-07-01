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
lmap_maybe = comp(list, map_maybe)

# for case_num in range(int(input())):