import numpy as np
from array import array
from random import random

#floats = array('d', (random() for i in range(10**7)))
floats = np.loadtxt('floats-10M-lines.txt')
# floats[-3:]
floats *= .5

from time import perf_counter as pc
t0 = pc(); floats /= 3
print(pc() - t0)

np.save('floats-10M', floats)