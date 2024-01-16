from collections import Counter

txt = "aaaaabbbbbccccccccccdddddeeeeeeeeeeeeeeee"
counter = Counter(txt)
print(counter)
print(counter.most_common(2))
print(counter.keys())
print(counter.values())
print(list(counter.elements()))
print(counter.get('a'))