def listproducts(list1, list2):
	productsum = 0
	for i in range(len(list1)):
		productsum += (list1[i] * list2[i])
	return(productsum)

def main():
	a = (input("Enter a list of numbers separated by spaces: "))
	b = (input("Enter another list of numbers separated by spaces: "))

	while len(a) != len(b):
		a = (input("Enter a list of numbers separated by commas: "))
		b = (input("Enter a list of numbers separated by commas: "))

	a1 = a.split(",")
	b1 = b.split(",")

	a2 = [eval(x) for x in a1]
	b2 = [eval(x) for x in b1]

	output = listproducts(a2, b2)
	print(output)

main()






