#  File: Intervals.py

#  Description: This program sorts through intervals that are represented as tupples 

#  Student Name: Derek Orji 

#  Student UT EID: dao584

#  Course Name: CS 303E

#  Unique Number: 51845

#  Date Created: 4/25/2017

#  Date Last Modified: 4/25/2017

def main():
	# main function this initial part reads in data from the text file
	in_file = open("intervals.txt", "r")
	list1 = []
	tuple1 = ()
	for line in in_file:
		line1 = line.strip()
		line2 = line1.split()
		a = int(line2[0])
		b = int(line2[1])
		tuple1 = (a, b)
		list1.append(tuple1)
	# This part sorts the tupples in ascending order
	for i in range(0, len(list1)):
		for j in range(i+1, len(list1)):
			if list1[i][0] < list1[j][0]:
				continue
			elif list1[i][0] == list1[j][0]:
				if list1[i][1] == list1[j][1]:
					continue
				elif list1[i][1] < list1[j][1]:
					continue 
				else:
					list1[i], list1[j] = list1[j], list1[i]
			else:
				list1[i], list1[j] = list1[j], list1[i]
	# This part shrinks the list of tupples down into non-intersecting intervals 
	list2 = []
	counter = 0
	start = list1[counter]
	initial = start[0]
	final = start[1]
	for i in range(len(list1)):
		if final >= list1[i][1]:
			counter += 1
			continue 
		if final < list1[i][1]:
			if list1[i][0] >= initial and list1[i][0] <= final:
				start = list1[i]
				final = start[1]
			else:
				list2.append((initial, final))
				start = list1[i]
				initial = start[0]
				final = start[1]

		else:
			list2.append((initial, final))
			start = list1[i]
			initial = start[0]
			final = start[1]
	list2.append((initial, final))
		

	print("Non-intersecting Intervals:\n", end = "")
	for item in list2:
		print(item)

	list3 = list2
	# This part figures out the lengths of the intervals and prints them in ascendind order
	for i in range(0, len(list3) - 1):
		for j in range(i+1, len(list3)):
			diff = abs(list3[i][1] - list3[i][0])
			if abs(list3[j][1] - list3[j][0]) < diff:
				list3[i], list3[j] = list3[j], list3[i]
			else:
				continue 
	print()
	print("Non-intersecting Intervals in order of size:\n", end = "")
	for item in list3:
		print(item)
Digit	Count	%
1	18	30.0
2	8	13.3
3	8	13.3
4	6	10.0
5	10	16.7
6	5	8.3
7	2	3.3
8	1	1.7
9	2	3.3

	
main()
