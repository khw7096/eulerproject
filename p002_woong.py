a = 1
b = 2
sum = 0
while a < 4000000:
	#print a + b	
	if (a+b)%2 == 0:
		sum = sum + (a + b) 
	a,b = b,a+b

print sum + 2
	
