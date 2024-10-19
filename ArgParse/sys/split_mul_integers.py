import sys 


def mul(val):
    val *= val
    return val

print ("the name of the program is", sys.argv[0]) 

a=sys.argv[1].split(' ')
n = len(a)
a=a[1:n] 

print(list(map(mul,map(int,a))))
