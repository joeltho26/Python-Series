from functools import reduce

val = [10,20,30]
total = reduce(lambda x,y:x*y,val)
print(total)
