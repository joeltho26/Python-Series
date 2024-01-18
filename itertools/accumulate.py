from itertools import accumulate
import operator

a = [5,10,20]
output = accumulate(a,func=operator.mul)
print(list(output))