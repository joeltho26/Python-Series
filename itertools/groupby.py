from itertools import groupby

a = [5,15,25,35,10,20,30,40]
output = groupby(a,key=lambda x: x%10==0)
for group,value in output:
    print(group,tuple(value))