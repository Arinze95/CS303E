#  File: Hailstone.py

#  Description: Program calculates the hailstone sequence for a range of numbers and outputs number with longest sequence and sequence length 

#  Student Name: Derek Orji

#  Student UT EID: dao584

#  Course Name: CS 303E

#  Unique Number: 51845

#  Date Created: 3/4/17

#  Date Last Modified: 3/4/17

# User Input for the first value to calculate hailstone seuence for
a = int(input("Enter starting number of the range: "))
# User input for the last value to calculate hailstone sequence for 
b = int(input("Enter ending number of the range: "))

# Conditions check that neither a or b is less than 0, also check that starting value is less than ending value. Contimue to prompt user until correct  
while (0 >= a) or (0 >= b) or (a >= b):
	a = int(input("Enter starting number of the range: "))
	b = int(input("Enter ending number of the range: "))




# main function takes in the values of the 1st and last number to calculate hailstone sequence for 
def main(a, b):
	
	#Initializing the value of the number that has the longest cycle length 
	jmax = 0
	# Initializing the value of the maximum number of steps (cycle length) to complete the hailstone sequence 
	cyclemax = 0

	# This loop calculates the sequence for each number from beginning(a), until end(b)
	for j in range(a, b+1):
		# because j is altered in the midst of the hailstone calculation, n stores the value of j
		n = j
		# initializes the value of the number of steps to complete the hailstone series for a specific number 
		cyclelen = 0

		# performs hailstone series operations on a number until the number is 1 
		while j > 1:
			
			# If the number is even perform the operation below and add 1 to the cycle length 
			if j % 2 == 0:
				j = j // 2
				cyclelen += 1
			# If the number is odd, perform the operation below and add 1 to the cycle length 
			elif j % 2 != 0:
				j = (3*j) + 1
				cyclelen += 1
			# Compares the currently calculated cycle length to the current maximum cycle length that has been calculated and re assigns max cycle length is necessary
			if (cyclelen >= cyclemax):
				cyclemax = cyclelen
				# Assigns a value to the number with the highest cycle length 
				jmax = n

	#Prints number with longest hailstone sequence and the length of the sequence 
	print("The number", jmax, "has the longest cycle length of", cyclemax)


main(a, b)

