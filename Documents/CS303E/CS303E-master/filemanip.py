def main():

	filerandom = open("randomfile.txt", "w")
	filerandom.write("I am the greatest basketball player that ever lived because I love to play basketball and basketball loves me, I love basketball basketball you dont love me basketball you hate me basketball lets rock and roll basketball yes")
	filerandom.close()

	filerandom = open("randomfile.txt", "r")
	newfile = (filerandom.readlines())
	print(newfile)

	forbidden = input("Give a list of the forbidden words: ").split()

	Bool = True 

	for word in forbidden:
		for i in range(len(newfile)):
			if word in newfile[i]:
				print("False")
				Bool = False 
				break 
		break
	if Bool == True:
		print("True")



	
main()