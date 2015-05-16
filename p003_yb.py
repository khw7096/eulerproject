import math

def factors(num):
	factorlimit = int(math.sqrt(num))
	factors = []
	for i in range(2, factorlimit+1):
		if num % i is 0:
			factors.append(i)

	return factors

def main():
	number = 600851475143
	f = factors(number)
	# print(f)
	primef = [i for i in f if not factors(i)]
	print(primef[-1])
	
	
main()