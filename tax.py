income = int(input("enter no"))

if income > 20000:
	x  = income - 20000
	tax1 = 10000/100 * 10
	tax2 = x/100 * 20
	tax = tax1 + tax2
	print(f"tax payable is {tax} ")

elif 10000 < income <= 20000:
	x = income - 10000
	tax = x/100 * 10
	print(f"tax payable is {tax} ")

else:
	print("tax payable is 0")

