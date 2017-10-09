import random
randlist1 = []
for i in range(0,1000):
	randlist1.append(random.randint(0,9))

counts = [0,0,0,0,0,0,0,0,0,0]
for i in range(0,10):
	addd = 0
	for j in range(len(randlist1)):
		if i == randlist1[j]:
			addd += 1
	counts[i] = addd
	

for i in range(len(counts)):
	print(i, "displays", counts[i], "times")

