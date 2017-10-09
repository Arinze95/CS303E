#  File: GuessingGame.py

#  Description: This program guesses numbers between 0 - 100 until it reaches the user's guess 

#  Student Name: Derek Orji

#  Student UT EID: dao584

#  Course Name: CS 303E

#  Unique Number: 51845

#  Date Created: 4/12/17

#  Date Last Modified: 4/12/17




def main():
	print("Guessing Game")
	print()
	#prompts user to guess
	prompt = "Think of a number between 1 and 100 inclusive. \nAnd I will guess what it is in 7 tries or less."
	print(prompt)
	print()
	#Checks their readiness to start program
	prepared = input("Are you ready? (y/n): ")
	print()
	while prepared != "y" and prepared != "n":
		prepared = input("Are you ready? (y/n): ")
		print()
	
	if prepared == "n":
		return(print("Bye"))
	if prepared == "y":
		# initial guess is always 50
		initialguess = input("Guess 1 : The number you thought was 50 \nEnter 1 if my guess was high, -1 if low, and 0 if correct: ")
		print()
		# resolicit user input if not entered correctly 
		while initialguess != "1" and initialguess != "0" and initialguess != "-1":
			initialguess = input("Guess 1 : The number you thought was 50 \nEnter 1 if my guess was high, -1 if low, and 0 if correct: ")
			print()
		
		
		lo = 0
		hi = 100
		counter = 1
		mid = 50
		# Reconfiguring guess based on user input
		while counter < 7:
			mid = (lo + hi) // 2
			if initialguess == "1":
				hi = mid - 1
				counter += 1
				mid = (lo + hi) // 2
				initialguess = input("Guess " + str(counter) + " : The number you thought was " + str(mid) + "\nEnter 1 if my guess was high, -1 if low, and 0 if correct: ")
				print()
				while initialguess != "1" and initialguess != "0" and initialguess != "-1":
					initialguess = input("Guess " + str(counter) + " : The number you thought was " + str(mid) + "\nEnter 1 if my guess was high, -1 if low, and 0 if correct: ")
					print()
			elif initialguess == "-1":
				lo = mid + 1
				counter += 1
				mid = (lo + hi) // 2
				initialguess = input("Guess " + str(counter) + " : The number you thought was " + str(mid) + "\nEnter 1 if my guess was high, -1 if low, and 0 if correct: ")
				print()
				while initialguess != "1" and initialguess != "0" and initialguess != "-1":
					initialguess = input("Guess " + str(counter) + " : The number you thought was " + str(mid) + "\nEnter 1 if my guess was high, -1 if low, and 0 if correct: ")
					print()
			elif initialguess == "0":
				return(print("Thank you for playing the Guessing Game."))
		# Ending outputs 
		if counter == 7 and initialguess == "0":
			print("Thank you for playing the Guessing Game.")
		else:
			print("Either you guessed a number out of range or you had an incorrect entry.")




  


main()