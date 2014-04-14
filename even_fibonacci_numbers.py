# Eden Ghirmai, 4/13/2014, projecteuler.net
# By considering the terms in the Fibonacci sequence
# whose values do not exceed four million, 
# find the sum of the even-valued terms.
def fib(n): 
	sum = 0
	a, b = 0, 1
	while b < n:
		if b % 2 == 0:
			sum += b
		a, b = b, a + b
	return sum	
		
print fib(4000000) 			

