s = input("Enter a single word: ")
ss = input("Enter another single word: ")
s1 = list(s)
s2 = list(ss)

Boolean = False
for i in range(len(s1)):
	if s1[i] not in s2:
		Boolean = True
		print("is not an anagram")
		break

if Boolean == False:
	print("is an anagram")