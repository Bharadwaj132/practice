# Print the sum of the current number and the previous number
#Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.
CurNum = 0
PrevNum = 0
 
for i in range(10):
	sum = CurNum+PrevNum
	print('Current Number', CurNum, 'Previous Number', PrevNum, 'sum', sum)
	PrevNum = CurNum
	CurNum = CurNum + 1



PrevNum = 0
 
for i in range(10):
	sum = i+PrevNum
	PrevNum = i
	i = i + 1
	print(sum)