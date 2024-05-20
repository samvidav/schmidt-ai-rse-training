import numpy as np
from functools import reduce
import re
from multiprocessing import Pool

def square_num(x):
    numx = 0
    if re.match("[-+]*[0-9]+", x):
        numx = x
    return int(numx)**2

def sum_of_nums(l):  
    # sum all the numbers
    return reduce(lambda a, b: a + b, l)

# Generate a list of numbers to add up
test_nums = list(map(str, range(1000+1)))

# Get the squares
if __name__ == '__main__':
    with Pool(8) as p:
        lsq = p.map(square_num, test_nums)
    print(sum_of_nums(lsq))
