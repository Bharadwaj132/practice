def reverseoder(int):
	reverse_num = 0

	while int > 0:
		reminder = int % 10
		int = int // 10

		print(reminder, end = " ")

reverseoder(7536)