num1 = input("enter_no")

num2 = num1[ : : -1]

if num1 == num2:
	print(f"Yes. {num1} is palindrome number")
else:
	print(f"No. {num1} is not palindrome number")


def palindrome(number):
	orginal_num = number
	reverse_num = 0

	while number > 0:
		reminder = number % 10
		reverse_num = (reverse_num * 10) + reminder
		number = number // 10
	
	if orginal_num == reverse_num:
		print(f"Yes. {orginal_num} is palindrome number")
	else:
		print(f"No. {orginal_num} is not palindrome number")


palindrome(int(input("enter no")))