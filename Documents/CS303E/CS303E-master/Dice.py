#  File: Dice.py
#  Description: Rolling of two six-sided die and output of their summations 
#  Student's Name: Derek Orji
#  Student's UT EID: dao584
#  Course Name: CS 313E 
#  Unique Number: 51465
#
#  Date Created: 9/13/17
#  Date Last Modified: 9/15/17

import random #Used for random dice rolls
import math #Used for some rounding/scaling operations

def main():
	random.seed(1314)
	combos = []; #Holds the sum of the two die rolls

	numtrials = int(input("How many times do you want to roll the dice? ")) #Retrieve number of trials from user 
	for i in range(numtrials):
		d1 = random.randint(1,6)
		d2 = random.randint(1,6)
		combos.append(d1+d2); #populated with sum of the two die rolls

	size = len(combos) #Used to loop through list of summed die rolls to count up repeated occurences
	
	outcome = [];
	outcome2 = [];
	for j in range(2,13,1): #looping through dual die rolls to count up number of times 2-12 is rolled
		counter = 0;
		for x in range(size):
			if j == combos[x]:
				counter += 1;
			else:
				continue 
		outcome.append(counter); #list of number of occurences of rolling sums 2-12

	print('Result:', outcome)
	max1 = max(outcome); #Retrieve number of times most commonly rolled sum occurs
	size1 = len(outcome);
	if numtrials <= 100: # printing histogram if number of trials is 100 or less then we print respective number of summed occurences as is
		for n in range(max1,0,-1):
			print("|", end ="  ")
			for m in range(0, size1):
				if outcome[m] >= n and m < size1-1:
					print("*", end ="  ")
				elif outcome[m] >= n and m == size1-1: #go to a new line if on 12
					print("*")
				elif outcome[m] < n and m < size1-1:
					print(end ="   ")
				elif outcome[m] < n and m == size1-1: #new line if on 12
					print("")
				else:
					continue 

	else: # if number of trials is greater than 100 then we scale down our histogram
		outcome3 = [];
		for v in range(0,size1):
			outcome2.append(outcome[v]*(100/numtrials)); # scaling of histogram values 
		for u in range(0, size1): # logic to round either up or down dependng on the value after the decimal place
			if outcome2[u] - (math.floor(outcome2[u])) < 0.5: #round down criteria
				outcome3.append(math.floor(outcome2[u]));
			elif outcome2[u] - (math.floor(outcome2[u])) >= 0.5: # round up criteria
				outcome3.append(math.ceil(outcome2[u]));
		max2 = max(outcome3)
		for n in range(max2,0,-1): #printing of scaled down histogram
			print("|", end ="  ")
			for m in range(0, size1):
				if outcome3[m] >= n and m < size1-1:
					print("*", end ="  ")
				elif outcome3[m] >= n and m == size1-1:
					print("*")
				elif outcome3[m] < n and m < size1-1:
					print(end ="   ")
				elif outcome3[m] < n and m == size1-1:
					print("")
				else:
					continue 

	
	print("+--+--+--+--+--+--+--+--+--+--+--+-") #formatting of x-axis of histogram
	for i in range(1,13):
		if i == 1:
			print("   ",end="")
		elif i == 10 or i == 11 or i ==12:
			print(i,"", end = "")
		else:
			print(i," ", end ="")

main()
		
		
