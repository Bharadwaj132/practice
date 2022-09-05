
x = 9
y = 2

print('1st program')
if x % y == 0:
	print(f"{x} is even")
else:
	print(f'{x} is odd')


x = 10

print('2st program')
if x % y == 1:
	print(f"{x} is odd")
else:
	print(f'{x} is even')

print('3rd program')
for x in range(10):
	if x % y == 0:
		print(f'{x}')

print('4th program')
for x in range(10):
	if x % y == 0:
		pass
	else:
		print(f'{x}')

print('5th program')
for x in range(10):
	if x % y == 0:
		print(f'{x} is even')
	else:
		print(f'{x} is odd')


print('6th program')
for x in range(0, 10, 2):
	print(f'{x}')

print('5th program')
for x in range(1, 10, 2):
	print(f'{x}')


print('7th program')
A = (1,2,3,5,6,7,4,8,)
b = 2

for i in A:
	if i % b == 1:
		print(f'{i} is odd')
	else:
		print(f'{i} is even')