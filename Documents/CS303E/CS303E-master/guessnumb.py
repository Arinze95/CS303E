import random
num = random.randint(0,100)
answer = eval(input("What is your guess for a number between 0 and 100 inclusive? "))
while answer != num:
	if answer > num:
		print("Your answer is too high")
		answer = eval(input("Guess another time, but lower now: "))
	else: 
		print("Your answer is too low")
		answer = eval(input("Guess another time, but higher now: "))
print("You\'re correct, the answer is", answer)



