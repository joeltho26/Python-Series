from itertools import product

a = [10,20]
b = [30,40]
op = product(a,b,repeat=2)
print(list(op))