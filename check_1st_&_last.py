def check_FL(list):
	print("list:", list)
	if list[0] == list[-1]:
		return 'result is True'
	else:
		return 'result is False'

print(check_FL(['apple', 'banana', 'cherry']))
print(check_FL(['apple', 'banana', 'apple']))
num_list = [10, 20, 30, 10]
print(check_FL(num_list))