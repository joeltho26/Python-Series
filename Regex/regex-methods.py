import re

text = "Hello, World! 123"
print(re.findall(r'[a-zA-Z0-9\,\s]+',text))
print(re.sub(r'[a-zA-Z]+','John',text,count=1))
print(re.match(r'[a-zA-Z0-9\,]+',text))
print(re.search(r'[a-zA-Z0-9]+',text))
pattern = re.compile(r'[a-zA-Z\s\!\,]+')
print(re.match(pattern,text))
print(re.split(r'\s',text,maxsplit=1))
print(re.fullmatch(r'[a-zA-Z0-9\s\!\,]+',text))
