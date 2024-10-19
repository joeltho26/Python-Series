import sys 

print("the name of the program is ", sys.argv[0]) 

a = sys.argv[1].split(' ')
n = len(a)
a = a[1:n] 
for i in a: 
	print(i)