import random 

# 1. Generate two random single-digit integers 
number1 = random.randint(0, 9)
number2 = random.randint(0, 9)


if number1 < number2:
	number1, number2 = number2, number1
	print("We had to reasign the numbers")
	print("Number 1 is",number1,"Number 2 is", number2)
	question = eval(input("What is Number 1 - Number 2? ")) 
else: 
	print("No need to reassign numbers")
	print("Number 1 is",number1,"Number 2 is", number2)
	question = eval(input("What is Number 1 - Number 2? ")) 

if number1 - number2 == question:
	print("Correct!")
if number1 - number2 != question: 
	print("Incorrect :(\n", number1,"-", number2, "is", number1 - number2)



