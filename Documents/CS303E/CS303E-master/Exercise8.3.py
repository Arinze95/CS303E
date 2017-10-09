password = input("Enter a password of atleast 8 characters, only letters and digits, and must have atleast 2 digits: ")

if len(password) >= 8 and password.isalnum() and (password.count("0") + password.count("1") + password.count("2") + password.count("3") + password.count("4") + password.count("5") + password.count("6") + password.count("7") + password.count("8") + password.count("9")) >= 2:
	print("valid password")
else:
	print("invalid password")

	