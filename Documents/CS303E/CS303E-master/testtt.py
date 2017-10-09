a = int(input("Enter starting number of the range: "))
b = int(input("Enter ending number of the range: "))

def main(a, b):
	for j in range(a, b+1):
		count = 0
		print(j, end = " ")
		while j > 1:
			
			if j % 2 == 0:
				j = j // 2
			elif j % 2 != 0:
				j = (3*j) + 1

			count += 1
			print(j, end = " ")
				
		print()
main(a, b)
		