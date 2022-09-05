b = 11
j = 0

for x in range(1, b+1):
	if b % x == 0:
		j = j + 1
	
print(j)
if j == 2:
	print(f'{b} is a prime')


num = 10
y = 0

for b in range(num):
	#print(b)
	j = 0
	for x in range(1, b+1):
		if b % x == 0:
			j = j + 1
	
	#print(j)

	if j == 2:
		y = y + 1
		print(f'{b} is a prime')
	else:
		print(f'{b} is not a prime')

print(y)