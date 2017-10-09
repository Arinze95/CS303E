lst = input("Enter a list: ").split()
print(lst)
newlist = []
for i in range(len(lst)):
	if lst[i] not in newlist:
		newlist.append(lst[i])
print(newlist)



