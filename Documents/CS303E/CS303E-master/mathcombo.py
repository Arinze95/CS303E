import random 
n = 0

for i in range(1,7):
	for j in range(2,8):
		if i != j and (j > i):
			print(i,j)
			n += 1 

print("The total number of all combinations is", n)




