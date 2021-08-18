from datetime import date, timedelta

colors = ['Bronze','Fuschia','Magenta','Olive','Lime','Salmon','Cyan','Amber']

# starting with the highest number (color), they add up the date
#    eg 2018-10-26 would be added to 2054
# and divide it by that number.
# If the modulus is 0, that is the color of the day.
# If not, they decrement by one until they reach a modulus of 0.

test = date(2018,10,26)
assert(sum([int(n) for n in str(test).split('-')]) == 2054)

target = date.today() - timedelta(days=123)
n = sum([int(n) for n in str(target).split('-')])

for val, col in reversed(list(enumerate(colors))):
    result = n % val
    if result == 0:
        print('Color is', col)
        break

# Cyan, GPSCTF{952a1af38062c22b7187c97a52ac9bec}