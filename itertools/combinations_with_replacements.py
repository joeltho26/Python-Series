from itertools import combinations_with_replacement

a = [10,20,30,40]
output = combinations_with_replacement(a,r=3)
print(list(output))