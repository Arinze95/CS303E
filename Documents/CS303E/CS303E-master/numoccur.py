def main():

	filerandom = open("randomfile.txt", "w")
	filerandom.write("I am the greatest basketball player that ever lived because I love to play basketball and basketball loves me, I love basketball basketball you dont love me basketball you hate me basketball lets rock and roll basketball yes")
	filerandom.close()

	dobbie = input("What file do you want to look at? ").strip()


	string1 = input("What word are you looking for: ").strip()

	filerandom = open(dobbie, "r")

	newfile = filerandom.readlines()
	count = 0
	for line in newfile:
		count += line.count(string1)

	print(string1, "appears", count, "times in", dobbie)

main()

