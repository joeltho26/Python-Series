list_a = [10,20,30,40,50]
list_b = list((10,20,30,40,50,60,70))
list_c = [89,49]
print(len(list_a))
print(list_b[:-1:])
print(list_b[::-1])
print(list_b[-6:-1:2])
for i in range(len(list_b)):
    print(list_b[i])
for i in range(0,len(list_b),2):
    print(list_b[i])
print(list_b)
list_a.append(60)
print(list_a)
list_a.extend(list_b)
print(list_a)
print(list_a[3])
print(list_c.pop(0))
print(list_c)
print(list_c.remove(49))
list_c.clear()
print(list_c)
list_b.insert(2,80)
print(list_b)
list_c = list_b.copy()
print(list_c.index(80))
print(list_c.count(10))
list_c.reverse()
print(list_c)
del list_c
list_c = ["Orange","Lemon","Watermelon"]
list_c.sort(key=lambda x: len(x), reverse=True)
print(list_c)

# list comprehension
list1 = ["Blueberry","Jackfruit","Banana"]
c = []
b = []
[c.append(i) if i.startswith("B") else b.append(i) for i in list1]
print(c)
print(b)
print([i for i in list1 if len(i) > 5])
print(sorted(b, key=lambda x: len(x), reverse=True))
print(list(reversed(b)))