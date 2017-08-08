from collections import defaultdict as dd
default = dd(int)
default['age'] += 1
print(default)
default['age'] = 39
default['age'] += 1
print(default)

