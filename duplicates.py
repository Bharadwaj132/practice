print('1st program')
A = [1,2,2,3,4,4,5]

print(set(A))

print(len(set(A)))


print('2nd program')
A = [1,2,2,3,4,4,5]

A = set(A)
print(A)


print('3rd program')
A = [1,2,2,3,4,4,5]
S = []

for i in A:
	if i not in S:
		S.append(i)
print(S)


print('4th program')
A = [1,2,2,3,4,4,5]
S = []

i = 0
while i < len(A):
	if A[i] not in S:
		S.append(A[i])
	i = i + 1
print(S)


import removeduplicates
removeduplicates.prog()
