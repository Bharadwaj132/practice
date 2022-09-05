enter = int(input('enter no'))

x = 0
y = 1
print(x)
print(y)

for i in range(enter - 2):
	z = x+y
	x = y
	y = z
	print(z)
