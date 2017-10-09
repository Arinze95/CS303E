def main():
	a = ([4, 9, 2], [3, 5, 7], [8, 1, 6])
	sum_n = 0
	for row in a:
		for col in row:
			sum_n += col
	print(sum_n)
main()