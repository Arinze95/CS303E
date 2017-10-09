#  File: Goldbach.py

#  Description: This is a program that displays all pairs of prime numbers that sum to equal a user defined number for a user defined range of numbers 

#  Student Name: Derek Orji

#  Student UT EID: dao584

#  Course Name: CS 303E

#  Unique Number: 51845

#  Date Created: 3/24/2017

#  Date Last Modified: 3/24/2017



# this function determines if a number is prime
def is_prime (n):
	if (n == 1):
		return False

	limit = int (n ** 0.5) + 1
	divisor = 2
	while (divisor < limit):
		if (n % divisor == 0):
			return False
		divisor += 1
	return True

def main():
	# User input for lower and upper limits of range 
	a = eval(input("Enter the lower limit: "))
	b = eval(input("Enter the upper limit: "))
	# both lower and upper limit must be even, lower limit must be less than upper limit, and lower limit must be greater than 4. If any of these aren't true, then re-prompt the user 
	while a < 4 or a % 2 != 0 or b % 2 != 0 or (b <= a):
		a = eval(input("Enter the lower limit: "))
		b = eval(input("Enter the upper limit: "))

	# gets pairs of prime numbers for every even number in user defined range 
	for i in range(a, b+1, 2):
		# eligible is a list that will hold all prime numbers less than a given number
		eligible = []
		print(i, end = " ")
		# we only populate eligible with those prime numbers that are up to half of the given number we are looking at 
		for j in range(2,i//2+1):
			if is_prime(j) == True:
				eligible += [j]
		# subtract eligible prime number from its given number to find the checker, the checker is then checked to see if it is prime 
		# if the checker is prime, then both it and its corresponding eligible number are a pair that sum up to the user defined number 
		for x in range(len(eligible)):
			checker = i - eligible[x]
			if is_prime(checker) == True:
				print("=", eligible[x], "+", checker, end = " ")
		print()


main()








