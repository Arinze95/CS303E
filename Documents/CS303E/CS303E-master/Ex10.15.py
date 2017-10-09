s = input("Enter list: ")
s1 = s.split()
lst = [int(x) for x in s1]
hasprinted = False 
for i in range(len(lst)-1):
	if (lst[i]) > (lst[i+1]):
		print("The list is not already sorted")
		hasprinted = True 
		break
if hasprinted == False: 
	print("The list is already sorted")
