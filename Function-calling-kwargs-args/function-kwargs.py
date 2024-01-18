def add(x,y,z):
    return x + y + z
print(add(5,y=10,z=20))

def mul(*args,**kwargs):
    val1, val2 = args
    return val1,val2,kwargs['y'],kwargs['z']
print(mul(3,5,y=10,z=20))   