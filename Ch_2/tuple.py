lax_coordinates = (33.945, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traverl_ids = [('USA', '31195855'), ('BRA', 'CE342567'),
               ('ESP', 'XDA205856')]

for passport in sorted(traverl_ids):
    print('%s/%s' %passport)

for country, _ in traverl_ids:
    print(country)
    
# Unpacking nested tuples to access the longitude
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:^9.4f} | {:^9.4f}'
for name, cc, pop, (lat, lon) in metro_areas:
    if lon  <= 0:
        print(fmt.format(name, lat, lon))