# Eden Ghirmai, www.projecteuler.net
# finds the largest prime factor of 600851475143

import math
def prime(n):
	for x in range (int(n / 2), 1, -1):
		if (n % x == 0):
			return x

	return -1		

print prime(600851475143)
