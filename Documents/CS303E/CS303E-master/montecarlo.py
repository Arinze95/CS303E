import random

numtrials = 1000000
numhits = 0

for i in range(numtrials):
	x = random.random() *2 - 1 
	y = random.random() *2 - 1

	if x * x + y * y <= 1:
		numhits += 1
pi = 4 * numhits / numtrials

print("PI is", pi)

