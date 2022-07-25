import array

numbers = array.array('h', [-2,-1,0,1,2])
memv = memoryview(numbers)
len(memv)