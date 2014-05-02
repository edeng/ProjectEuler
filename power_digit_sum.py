# Eden Ghirmai, www.projecteuler.net, 5/1/2014
# prints the sum of digits of the number 2^1000

num = 2**1000
total = 0; 
while num != 0:
	total += num % 10
	num /= 10

print total	
