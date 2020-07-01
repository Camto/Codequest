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
	def comp2(f, g):
		return lambda x: f(g(x))
	return reduce(comp2, funcs, lambda x: x)

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

concat_ = lambda lists: reduce(concat, lists)

alpha = "abcdefghijklmnopqrstuvwxyz"
fbool = lambda b: str(b).lower()
rbool = lambda s: s == "true"

get_in = lambda: sys.stdin.readline().rstrip()

cases = int(get_in())
for case_num in range(cases):