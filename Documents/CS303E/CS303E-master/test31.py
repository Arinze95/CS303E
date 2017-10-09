
#def main():
#	a = [[1, 2, 3], [4,5,6], [7,8,9], [6,0,8], [3,4,5], [1,0,6]]
#	c = []
#	for i in range(len(a)-1, -1, -1):
#		d = []
##			d.append(a[i][j])
#		c.append(d)
#		

#	return(print(c))





		
#main()
def main():
	a = [12, 7, 3, 4, 10, 6, 8]
	for i in range(len(a)-1):
		for j in range(i+1, len(a)):
			if a[j] < a[i]:
				a[i], a[j] = a[j], a[i]
			else:
				continue 
	return(print(a))
	
main()


