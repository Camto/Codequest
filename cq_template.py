import sys
import math
import string
import re

from functools import *
from itertools import *
from operator import *

lmap = lambda *args: list(map(*args))
lfilter = lambda *args: list(filter(*args))
lrange = lambda *args: list(range(*args))
lreversed = lambda *args: list(reversed(*args))

def comp(*funcs):
	comp2 = lambda f, g: lambda x: f(g(x))
	return reduce(comp2, funcs)

const = lambda val: lambda _: val

tuplefy = lambda f: lambda args: f(*args)
untuplefy = lambda f: lambda *args: f(args)

def curry(n, f):
	def wrap(*args):
		if n > len(args):
			return curry(n - len(args), lambda *largs: f(*args, *largs))
		return f(*args)
	return wrap

curried = curry(2, curry)

concat_ = partial(reduce, concat)

alpha = "abcdefghijklmnopqrstuvwxyz"
fbool = comp(str.lower, str)
rbool = partial(eq, "true")

cases = int(input())
for case_num in range(cases):