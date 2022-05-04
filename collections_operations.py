from collections import Counter
from collections import defaultdict
from collections import OrderedDict

s = 'heeellooo'
od = OrderedDict()
dd = defaultdict()
c = Counter(s)

for i in s:
    if i in od: od[i] += 1
    else: od[i] = 1
od['h'] += 1
print('OrderedDict: ')
print(od)

for i in s:
    if i in dd: dd[i] += 1
    else: dd[i] = 1
dd['h'] += 1
print('\ndefaultdict: ')
print(dd)

print('\nCounter')
print(c.most_common)

for i in s:
    dd[i] += 1

print(dd)