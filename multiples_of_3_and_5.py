# Eden Ghirmai, www.projecteuler.net
#  prints the sum of all the numbers divisible by 3 or 5
# from 1 to 1000

sum = 0 
for x in range(1000):
	if (x % 3 == 0 or x % 5 == 0):
		sum += x

print sum		
