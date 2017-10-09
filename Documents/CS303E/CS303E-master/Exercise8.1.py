SSN = input("Enter your Social Security number in the format ddd-dd-dddd, where d is a digit: ")



if len(SSN) == 11 and ord(SSN[3]) == 45 and ord(SSN[6]) == 45 and SSN[0:3].isdigit() and SSN[4:6].isdigit() and SSN[7:11].isdigit():
	print("Valid SSN")
else:
	print("Invalid SSN")
	

