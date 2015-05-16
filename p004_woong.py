import math

def chkmr(str):
	length = len(str)/2
	if str[0:length] == str[length:][::-1]:
		return 0
	else:
		return 1

def gennum(min, max):
	list = []
	for i in range(min, max):
		for j in range(min, max):
			list.append(i * j)
	return list

def main():
	chkmr("100100")
	plist = []
	for i in gennum(100, 1000):
		if len(str(i)) % 2 == 0 and chkmr(str(i)) == 0:
			plist.append(i)
		else:
			pass

	print max(plist)

main()
