from itertools import cycle, repeat, count

input = [10,20,30,40]
j = 0
for i in cycle(input):
    if j > 15:
        break
    print(i,j)
    j += 1
  
k = 0  
for i in repeat(input,2):
    print(i,k)
    k += 1
    
l = 0
for i in count(1):
    if l > 20:
        break
    print(i,l)
    l += 1
    