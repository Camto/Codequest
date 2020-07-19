## Imports.

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

# Bool formatting and reading.
fbool = comp(str.lower, str)
rbool = partial(eq, "true")

# Make a matrix.
matrix = lambda cols, rows, val: lmap(lambda _: [val] * cols, range(rows))

# Split list into chunks.
chunks = lambda l, n: [l[i * n:(i + 1) * n] for i in range((len(l) + n - 1) // n)]

# Shorter list conversion.
lmap = comp(list, map)
lfilter = comp(list, filter)
lrange = comp(list, range)
lreversed = comp(list, reversed)
lenumerate = comp(list, enumerate)
lmap_maybe = comp(list, map_maybe)

## Input parsing.

# Parse all the problem's input at once.
def parse_str(s, *expect_types):
	if len(expect_types) > 1:
		inp = s.split(" ")
		return tuple(map(tuplefy(parse_str), zip(inp, expect_types)))
	
	expect_type = expect_types[0]
	if expect_type in [int, float, str]:
		return expect_type(s)
	elif expect_type is bool:
		return rbool(s)
	elif type(expect_type) is str:
		return re.findall(expect_type, s)
	# They needs more input lines to parse.
	elif type(expect_type) is tuple:
		return (parse_str(s, expect_type[0]),) + tuple(map(get_in, expect_type[1:]))
	elif type(expect_type) is list:
		return lmap(lambda _: get_in(*expect_type), range(int(s)))

# Parse from input()
get_in = lambda *expect_types: parse_str(input(), *expect_types)