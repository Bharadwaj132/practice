str = '[dsjkfsh(djksl{sada})]'

for i in str:
	if i.isalpha() is True:
		str = str.replace(i, '')
print(str)
n = len(str)
dict = {"{": "}", "[": "]","(": ")"}
bal = None

if n % 2 != 0:
	print('parentheses is not balanced')
else:
	for i in range(n//2):
		print(dict.get(str[i]) == str[n-(i+1)])
		if dict.get(str[i]) == str[n-(i+1)]	:
			bal = True
		else:
			bal = False
			break	
if bal == True:
	print('parentheses is balanced')
else:
	print('parentheses is not balanced')


str  = '[dsjkfsh(djksl){sada(}])'

for i in str:
	if i.isalpha() is True:
		str = str.replace(i, '')
print(str)
n = len(str)
dict = {"{": "}", "[": "]","(": ")"}
nstr = []

for i in str:
	if i in ['(','[','{']:
		nstr.append(i)
		print(nstr)
	elif i in [')',']','}']:
		#print(i, dict.get(nstr[-1]))
		if len(nstr)> 0 and i == dict.get(nstr[-1]):
			nstr.pop()
		else: 
			nstr.append(i)
			print(nstr)
			break
		print(nstr)

if len(nstr) == 0:
	print('balanced')
else:
	print('not balanced')