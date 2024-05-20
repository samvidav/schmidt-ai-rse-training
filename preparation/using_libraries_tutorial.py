import math

print ('pi is', math.pi)
print('cos(pi) is', math.cos(math.pi))

# help(math)

# Imports only specific modules
from math import cos, pi
# Can then use directly
print('cos(pi) is', cos(pi))

# Imports with aliases
import math as m
print('cos(pi) is', m.cos(m.pi))

# EXERCISES

import random
bases = 'ACTTGCTTGAC'
bases[random.randint(0, len(bases))]

import math as m
angle = m.degrees(m.pi / 2)
print(angle)

