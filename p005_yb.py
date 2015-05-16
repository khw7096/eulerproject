def divByNums(num):
	for i in range(1, 21):
		if num % i is not 0:
			return False
		print(i)	
	return True

i = 1
for i in range(1, 300000000):
	if divByNums(i):
		break
	i = i+1

print(i)
