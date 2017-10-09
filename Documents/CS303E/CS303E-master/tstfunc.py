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



def main():
	number = int(input("Enter a 15 or 16 digit number: "))
	print(is_valid(number))
main()