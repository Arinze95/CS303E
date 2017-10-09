userinput = eval(input("Enter a number of your choice from 1 to 15"))

for i in range(1, userinput + 1, 1):
	for j in range(i, -(i+1), -1):
		if (j != 0 and j !=-1):
			print(abs(j), end = " ")
	print()
