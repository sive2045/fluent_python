colors = ['balck', 'white']
sizes = ['S', 'M', 'L']

# listcomp
tshirts = [(color, size) for color in colors 
                         for size in sizes]
print(tshirts)

# genexp
symbols = 'asdfv'
genexp = tuple(ord(symbol) for symbol in symbols)
print(genexp)

import array
array.array('I', (ord(symbol) for symbol in symbols))