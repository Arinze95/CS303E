#  File: ISBN.py

#  Description: This program determines the validity of ISBN codes 

#  Student Name: Derek Orji

#  Student UT EID: dao584

#  Course Name: CS 303E

#  Unique Number: 51845

#  Date Created: 4/13/17

#  Date Last Modified: 4/14/17

# Function to determine validity 
def validisbn(line2):
	a = []
	s1 = []
	s2 = []
	for i in line2:
		if i == "X" or i == "x":
			a.append(10)
		else:
			a.append(int(i))
	
	for i in range(0, len(a)):
		s1.append(sum(a[0:(i+1)]))
	for j in range(0, len(s1)):
		s2.append(sum(s1[0:(j+1)]))
	if (s2[len(s2)-1]) % 11 == 0:
		return True 
	else:
		return False

	


# Main function
def main():
	# Opening Files 
	initialfile = open("isbn.txt", "r")
	outputfile = open("isbnOut.txt", "w")
	# Checks that only digits, hyphens, and X's are available
	for line in initialfile:
		line1 = line.strip()
		valid = True
		for i in range(0,len(line1)):
			if line1[i] != "0" and line1[i] != "1" and line1[i] != "2" and line1[i] != "3" and line1[i] != "4" and line1[i] != "5" and line1[i] != "6" and line1[i] != "7" and line1[i] != "8" and line1[i] != "9" and line1[i] != "-" and line1[i] != "X" and line1[i] != "x":
				outputfile.write(line1 + "  invalid\n")
				valid = False
				break
				
		if valid == True: 
			
			
			#Checks for 9 digits and checks last character 
			counter = 0
			for i in range(0, (len(line1)-1)):
				if line1[i] == "0" or line1[i] == "1" or line1[i] == "2" or line1[i] == "3" or line1[i] == "4" or line1[i] == "5" or line1[i] == "6" or line1[i] == "7" or line1[i] == "8" or line1[i] == "9":
					counter += 1
			if counter != 9 or (line1[len(line1)-1] != "0" and line1[len(line1)-1] != "1" and line1[len(line1)-1] != "2" and line1[len(line1)-1] != "3" and line1[len(line1)-1] != "4" and line1[len(line1)-1] != "5" and line1[len(line1)-1] != "6" and line1[len(line1)-1] != "7" and line1[len(line1)-1] != "8" and line1[len(line1)-1] != "9" and line1[len(line1)-1] != "X" and line1[len(line1)-1] != "x"):
				outputfile.write(line1 + "  invalid\n")
			else:
				line2 = line1.replace("-", "")
				if validisbn(line2) == True:
					outputfile.write(line1 + "  valid\n")
				else:
					outputfile.write(line1 + "  invalid\n")
	#Closing Files 
	initialfile.close()
	outputfile.close()



main()
