dna2 = [5, 6, 3, 8]
for i in range(len(dna2)):
	print(i)
	count = 0
	endcounter = len(dna2)
	while endcounter > i:
		substrand = dna2[i:endcounter]
		endcounter = len(dna2) - 1
		count += 1
		print(substrand)
		