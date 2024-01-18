dict_a = {"firstname": "John",
          "age": 27,
          "gender": "Male",
          "color": 'Black',
          }

dict_b = dict(nationality="Canadian",lastname="Maison")
dict_a.update(dict_b)
print(dict_a)
print(dict_a['age'])
dict_c = dict_a.copy()
print(dict_c)
print(dict_a.get('firstname'))
print(dict_a.pop("color"))
print(dict_a)
print(dict_a.keys())
print(dict_a.values())
keys = ['previous_age','after_age']
values = 10
print(dict.fromkeys(keys,values))
dict_c.clear()
print(dict_c)
print(dict_b.items())
print(dict_a.popitem())
print(dict_a)
del dict_b
print(dict_b)