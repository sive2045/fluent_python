from array import array
from random import random

# creating a large array of floats
floats = array('d', (random() for i in range(10**7)))
print(floats[-1])
# saving
fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()
#loading
floats2 = array('d')
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10**7)
fp.close()
print(floats2[-1])
print(floats == floats2)