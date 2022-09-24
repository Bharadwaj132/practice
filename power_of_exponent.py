
base = 2
exponent = 5

print(base,"raises to the power of", exponent, "is",base ** exponent)

def power(base,exponent):
	num = exponent

	result = 1
	while num > 0:
		result = result * base
		num = num - 1
	print(base,"raises to the power of", exponent, "is",result)

power(5,4)