def prefix(s1, s2):
s1 = input("Enter a string: ")
s2 = input("enter a string: ")
N = " "
if len(s2) > len(s1):
	for i in range(len(s1)):
		if s1[0:i] == s2[0:i]:
			N = s1[0:i]
	print("The common prefix is", N)
if len(s1) > len(s2):
	for i in range(len(s2)):
		if s2[0:i] == s1[0:i]:
			N = s2[0:i]
	print("The common prefix is", N)
else:
	print("No common prefix")



