import math

a = 600851475143
def getprime(num):
	list = []
	for i in range(2, int(math.sqrt(num))):
		if num % i == 0:
			list.append(int(i))
	return list

for i in getprime(a):
	print i, getprime(i)






