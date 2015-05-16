import math

def gen_primes():
    D = {}  
    q = 2  
    while q < 100000000: #105000
        if q not in D:
            yield q        
            D[q * q] = [q]
        else:
            for p in D[q]:
				D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1

a = 1
for i in gen_primes():
	print a, i
	a = a + 1


#not understand
