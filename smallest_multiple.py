# Eden Ghirmai, 4/14/2014, projecteuler.net
# Find the smallest positive number that 
# is evenly divisible by all of the numbers from 1 to 20
def divisible(min, max, num):
	for x in range (min, max):
		if (num % x != 0):
			return False
	return True
x = 0
while True:
	x += 20
	if(divisible(1, 20, x)):
		print x	
		break		

