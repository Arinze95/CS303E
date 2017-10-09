#  File: Craps.py

#  Description: This is a simulation of rounds of the Craps game.

#  Student Name: Derek Orji

#  Student UT EID: dao584

#  Course Name: CS 303E

#  Unique Number: 51845

#  Date Created: 2/22/2017

#  Date Last Modified: 2/23/2017

import random

def craps():
	# Phase 1 - Comeout Phase
	die1comeout = random.randint(1,6)
	die2comeout = random.randint(1,6)
	
	# Summing the results of the dice rolls 
	comeoutrollresult = die1comeout + die2comeout

	# Conditions to determine if Craps round was won in the come out phase

	#Returns 1 for win if sum of 7 or 11 is rolled in comeout
	if (comeoutrollresult == 7) or (comeoutrollresult == 11): 
		return(1) 

	#Returns 0 for loss if sum of 2,3, or 12 is rolled in comeout
	elif (comeoutrollresult == 2) or (comeoutrollresult == 3) or (comeoutrollresult == 12): 
		return(0)
	else: # Phase 2 - Point Phase 
		die1pointphase = random.randint(1,6)
		die2pointphase = random.randint(1,6)

		# Summing the results of the point phase 
		pointphasesum = die1pointphase + die2pointphase

		# getting new random dice values if the player doesn't win or lose based on new sum and checks to see win or loss
		while (pointphasesum != 7 and pointphasesum != comeoutrollresult):  
				die1pointphase = random.randint(1,6)
				die2pointphase = random.randint(1,6)
				pointphasesum = die1pointphase + die2pointphase
		if pointphasesum == 7:
			return(0)
		elif pointphasesum == comeoutrollresult:
			return(1)
				
			
def main():
  # prompt the user to enter the number of rounds
  num_rounds = int (input ("Enter number of rounds: "))

  # compute the number of times he wins 
  num_wins = 0
  for n in range (num_rounds):
    num_wins += craps()

  # print the result
  print ("Player wins", num_wins, "out of", num_rounds, "rounds.")

main()






