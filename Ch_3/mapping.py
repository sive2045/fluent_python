import collections

my_dict = {}
print(isinstance(my_dict, collections.Mapping))

# What is Hashable?
tt = (1, 2, (30, 40))
hash(tt)

tl = (1, 2, [30, 40])
hash(tl) # unhashable type: 'list'

tf = (1, 2, frozenset([30, 40]))
hash(tf)

# dict Comprehensions
DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (55, 'Brazil'),
    (100, 'Korea')
]

country_code = {country:code for code, country in DIAL_CODES}