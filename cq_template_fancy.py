## Imports

# Basic imports.
import sys
import math
import string
import re

# Functional imports.
from functools import *
from itertools import *
from operator import *

## Composition related.

# Function composition.
comp = lambda *funcs: reduce(lambda f, g: lambda *x: f(g(*x)), funcs)

# To compose multiargument functions easier.
tuplefy = lambda f: lambda args: f(*args)
untuplefy = lambda f: lambda *args: f(args)

## Utility functions.

# Map and filter combined.
map_maybe = lambda *args: filter(partial(ne, None), map(*args))

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

## Input parsing.

# Parse all the problem's input at once.
def parse_str(expect_type, s):
	if expect_type in [int, float, str]:
		return expect_type(s)
	elif expect_type is bool:
		return rbool(s)
	elif type(expect_type) is tuple:
		inp = s.split(" ")
		return tuple(map(tuplefy(parse_str), zip(expect_type, inp)))
	elif type(expect_type) is list:
		# List needs more input lines to parse.
		return lmap(lambda _: get_in(expect_type[0]), range(int(s)))

# Parse from input()
get_in = lambda expect_type: parse_str(expect_type, input())