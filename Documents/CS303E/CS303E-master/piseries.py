_sum = 0
for i in range(1, 100001, 1):
	piii = 4 * ((-1)**(i+1))/((2*i)-1)
	_sum += piii

	if i % 10000 == 0:
		print(_sum)

		




	