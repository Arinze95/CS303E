#  File: CreditCard.py

#  Description: This program identifies credit cards by number from different companies 

#  Student Name: Derek Orji

#  Student UT EID: dao584

#  Course Name: CS 303E

#  Unique Number: 51845

#  Date Created: 4/6/17

#  Date Last Modified: 4/7/17

# This function checks if a credit card number is valid
def is_valid (cc_num):
	lengthcc_num = len(str(cc_num)) 
	counter = 0
	lsteven = []
	lstodd = []
	numberrr = cc_num
	while lengthcc_num > counter:
		evaluate = numberrr % 10
		if counter % 2 == 0:
			lsteven.append(evaluate)
		else: 
			doubledigit = 2 * evaluate
			if doubledigit // 10 != 0 or doubledigit == 10:
				digit1 = doubledigit % 10
				digit2 = doubledigit // 10
				sumdigit = digit1 + digit2
				lstodd.append(sumdigit)
			else:
				lstodd.append(doubledigit)
		counter += 1
		numberrr = numberrr // 10
	checker = sum(lstodd) + sum(lsteven)
	if checker % 10 == 0:
		return True 
	else:
		return False  

# This function returns the type of credit card
def cc_type (cc_num):
	s = str(cc_num)
	if ((s[0] + s[1]) == "34") or ((s[0] + s[1]) == "37"):
		return(" American Express")
	elif ((s[0] + s[1] + s[2] + s[3]) == "6011") or ((s[0] + s[1] + s[2]) == "644") or ((s[0] + s[1]) == "65"):
		return(" Discover")
	elif ((s[0] + s[1]) == "50") or ((s[0] + s[1]) == "51") or ((s[0] + s[1]) == "52") or ((s[0] + s[1]) == "53") or ((s[0] + s[1]) == "54") or ((s[0] + s[1]) == "55"):
		return(" MasterCard")
	elif (s[0] == "4"):
		return(" Visa")
	else:
		return("")



# This is the main program function that calls the sub functions 
def main (): 
	number = int(input("Enter a 15 or 16 digit number: "))
	lennumber = len(str(number))
	if lennumber < 15 or lennumber > 16:
		print("Not a 15 or 16-digit number")
		return  
	if is_valid(number) == False:
		print("Invalid credit card number")
	if is_valid(number) == True:
		print("Valid"+cc_type(number)+" credit card number")

main()