NewPhonenumber = input("Enter a phone number: ")
Phonenumber = NewPhonenumber.lower()
newnumber = " "
for i in range(0, len(Phonenumber)):
	if Phonenumber[i] == "a" or Phonenumber[i] == "b" or Phonenumber[i] == "c":
		newnumber += "2"
	elif Phonenumber[i] == "d" or Phonenumber[i] == "e" or Phonenumber[i] == "f":
		newnumber += "3"
	elif Phonenumber[i] == "g" or Phonenumber[i] == "h" or Phonenumber[i] == "i":
		newnumber += "4"
	elif Phonenumber[i] == "j" or Phonenumber[i] == "k" or Phonenumber[i] == "l":
		newnumber += "5"
	elif Phonenumber[i] == "m" or Phonenumber[i] == "n" or Phonenumber[i] == "o":
		newnumber += "6"
	elif Phonenumber[i] == "p" or Phonenumber[i] == "q" or Phonenumber[i] == "r" or Phonenumber[i] == "s":
		newnumber += "7"
	elif Phonenumber[i] == "t" or Phonenumber[i] == "u" or Phonenumber[i] == "v":
		newnumber += "8"
	elif Phonenumber[i] == "w" or Phonenumber[i] == "x" or Phonenumber[i] == "y" or Phonenumber[i] == "z":
		newnumber += "9"
	else:
		newnumber += Phonenumber[i]
print(newnumber)

