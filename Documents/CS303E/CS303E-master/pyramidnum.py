for i in range(1,7):
	for j in range(i, -(i+1), -1):
		if (j != 0 and j != -1):
			print(abs(j), end = " ")
	print()