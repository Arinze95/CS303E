def rotation(word, number):
	rotatedword = ''
	for i in range(len(word)):
		rotatedword += word[i - number]
	return rotatedword 

def main():
	userinputword = input("Enter a word: ")
	userinputnumber = eval(input("How much do you want to rotate the word by? "))
	output = rotation(userinputword, userinputnumber)
	print(output)
main()



