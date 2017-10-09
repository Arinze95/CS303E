def oneofone(list1):

list2 = []
for i in range(len(list1)):
	if list1[i] not in list2:
		list2.append(list1[i])

for i in range(0,len(list2)):
	print(list2[i], end = " ")
	



