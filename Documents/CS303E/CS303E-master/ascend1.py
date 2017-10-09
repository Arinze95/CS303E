def ascendlist(list1):

	for i in range(len(list1)-1):
		if list1[i] <= list1[i+1]:
			continue
		else:
			return False
			break 
	return True 

def main():
	s = input("Enter numbers separated by spaces: ").split()
	lst = [eval(x) for x in s]

	if ascendlist(lst):
		print("True")
	else: 
		print("False")
main()


