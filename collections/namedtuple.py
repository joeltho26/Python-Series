from collections import namedtuple

Point = namedtuple('Value','x,y,z')
pt = Point(10,20,30)
print(pt.x,pt.y,pt.z)
