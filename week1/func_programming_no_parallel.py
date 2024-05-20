import numpy as np
from functools import reduce
import re

def sum_of_squares(l):  
    # filter only to strings that can be cast to integers
    lnum = list(filter(lambda x: re.match("[-+]*[0-9]+", x), l))
    # square each number with map but cast the strings to int first
    lsq = list(map(lambda x: int(x)**2, lnum))
    # sum all the squared numbers
    return reduce(lambda a, b: a + b, lsq)

# Generate a list of numbers to add up
add_num = map(str, range(1000+1))
print(sum_of_squares(add_num))

