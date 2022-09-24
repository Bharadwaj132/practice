# Return the count of a given substring from a string

str_x = "Emma is good developer. Emma is a writer"

x = str_x.count("Emma")

print(f'Emma appered {x} times ')

def count_Emma(statement):
	print("Given string :", statement)
	count = 0
	for i in range(len(statement)):
		if statement[i: i+4] == 'Emma':
			count = count + 1
	return count

count = count_Emma(str_x)
print(f'Emma appered {count} times ')
