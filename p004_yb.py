def main():
	penlins = []
	# penlins = [i for i in range(10000, 1000000) if str(i)[::-1] == str(i)]
	penlins = [int(''.join([str(i), str(i)[::-1]])) for i in range(100, 1000)]
	print penlins
	penlins.reverse()

	find = 0
	for i in penlins:
		for j in range(100, 1000):
			if i % j == 0 and 100 <= i/j <1000:
				find = 1
				print(i,j,i/j)
				break
		if find:
			break


main()