#  File: DNA.py

#  Description: Finds the longest common sequence between two strands of DNA 

#  Student Name: Derek Orji

#  Student UT EID: dao584

#  Course Name: CS 303E

#  Unique Number: 51845

#  Date Created: 3/28/2017

#  Date Last Modified: 3/28/2017



def oneofone(list1):

	list2 = []
	for i in range(len(list1)):
		if list1[i] not in list2:
			list2.append(list1[i])
	return list2


def main():
	# Open file for reading 
	in_file = open("./dna.txt", "r")


	# read number of pairs 
	num_pairs = in_file.readline()
	num_pairs = num_pairs.strip()
	num_pairs = int(num_pairs)
	print("Longest Common Sequences")
	print()


	# read each pair of DNA strands 

	for i in range(num_pairs):
		st1 = in_file.readline().strip()
		st2 = in_file.readline().strip()
		
		# Make sure everything is capitalized 
		if len(st1) > len(st2):
			dna1 = st1.upper() 
			dna2 = st2.upper()
		else:
			dna1 = st2.upper()
			dna2 = st1.upper()
		

		# Get all substrings of dna2
		sequences = []
		start_idx = 0
		while (start_idx < len(dna2)):
			wnd = len(dna2)
			
			while((start_idx + wnd) > start_idx):
				substrand = dna2[start_idx:start_idx + wnd]
				sequences.append(substrand)
				
				wnd = wnd - 1
			start_idx = start_idx + 1 
		

		usequence = []
		#Get the unique substrands
		for j in range(len(sequences)):
			if sequences[j] not in usequence:
				usequence.append(sequences[j])
		

		#Longest Common Sequence 
		candidates = []
		for n in range(len(usequence)):
			if dna1.find(usequence[n]) != -1:
				candidates.append(usequence[n])
		


		# If candidates is populates then populate length list to find longest unique substrand 
		if len(candidates) > 0:
			length = []	
			for x in range(len(candidates)):
				length.append(len(candidates[x]))
		candidates = oneofone(candidates)

		# Look for elements of the max length in candidates 
		maxlength = max(length)
		if len(candidates) > 0:
			print("Pair "+str(i+1)+":", end = " ")
			for z in range(len(candidates)):
				if len(candidates[z]) == maxlength:
					print(candidates[z], end = "\n        ")
			

		# No commanalities 	
		else:
			print("Pair "+str(i+1)+":", "No Common Sequence Found")
		print()	
	

main()
