def add(value):
    out = lambda x: x + value
    return out

val = add(10)
print(val(20))

output = lambda x,y: x*y
print(output(10,20))

def divide(val):
    return val//2

op = lambda x: x * divide(40)
print(op(5))
