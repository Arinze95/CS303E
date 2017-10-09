# File: Deal.py

# Description: Monty Python Simulation of switching 

# Student Name: Derek Orji

# Student UT EID: dao584

# Course Name: CS 303E

# Unique Number: 51845

# Date Created: 2/27/2017

# Date Last Modified: 2/28/2017

import random

#User input for number of rounds that they'd like to play 
rounds = int(input("Enter number of times you want to play: "))
num_rounds = rounds 
print()

# wins variable records the number of times user wins by switching 
wins = 0 
print(format("  Prize", "<12s"), format("Guess", "<11s"), format("View", "<7s"), "New Guess")
while(num_rounds > 0):
	# variabe prize_door generates door number that prize will be behind 
	prize_door = random.randint(1,3)

	# variable contestant_guess generates contestant's guess
	contestant_guess = random.randint(1,3)

	# view is a variable that shows the door that monty hall opens, not the prize door and not the contestant's guess
	view = 0 
	if prize_door == 1 and contestant_guess == 1:
		view = random.randint(2,3)
	elif (prize_door == 1 and contestant_guess == 2) or (prize_door == 2 and contestant_guess == 1):
		view = 3
	elif (prize_door == 1 and contestant_guess == 3) or (prize_door == 3 and contestant_guess == 1):
		view = 2
	elif prize_door == 2 and contestant_guess == 2:
		view = random.randrange(1,4,2)
	elif (prize_door == 2 and contestant_guess == 3) or (prize_door == 3 and contestant_guess == 2):
		view = 1
	elif prize_door == 3 and contestant_guess == 3:
		view = random.randint(1,2)

	# new_guess variable that stores contestant's new guess, this is what the character chooses by switching 
	new_guess = 0
	if (contestant_guess == 1 and view == 2) or (contestant_guess == 2 and view == 1):
		new_guess = 3
	if (contestant_guess == 1 and view == 3) or (contestant_guess == 3 and view == 1):
		new_guess = 2
	if (contestant_guess == 2 and view == 3) or (contestant_guess == 3 and view == 2):
		new_guess = 1 

	# Check to see if user won by switching 
	if new_guess == prize_door: 
		wins += 1 

	print("   ",format(prize_door,"<10"),format(contestant_guess,"<10"), format(view,"<10"), new_guess)
	
	num_rounds -= 1

# Calculating probability of winning by switching and that of not switching 
probabilityofwinning = (wins/rounds) 
print()
print("Probability of winning if you switch =", format(probabilityofwinning,".2f"))
print("Probability of winning if you do not switch =", format((1 - probabilityofwinning),".2f"))











