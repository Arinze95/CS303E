listintiial = input("Enter a list of numbers between 1 and 100 seperated by spaces: ")

list1 = listintiial.split()
lst = [eval(x) for x in list1]

for i in range(2,100,1):
	count = lst.count(i)
	if count > 1:
		print(i, "occurs", count, "times")
	elif count == 1:
		print(i, "occurs", count, "time")


