from itertools import count
from itertools import cycle

for el in count(7, 1):
    if el < 100:
        print(el)
    else:
        break

c = 0
for el in cycle('Alisa'):
    if c > 100:
        break
    print(el)
    c += 1
