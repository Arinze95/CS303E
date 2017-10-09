def main():
	b = [[4,9,2], [3,5,7], [8,1,6]]
	e = [[1,1,1], [2,2,2], [3,3,3]]
	print(b[1])
	sumn = 0
	for i in range(len(b)):
		for j in range(len(b[i])):
			sumn += b[i][j]
	print(sumn)

	maxn = b[0][0]
	for i in range(len(b)):
		for j in range(len(b[i])):
			if b[i][j] > maxn:
				maxn = b[i][j]
			else:
				continue
	print(maxn)

	c = []
	for i in range(len(b)):
		d = []
		for j in range(len(b[i])):
			d.append(b[i][j])
		c.append(d)
	print(c)

	#transpose a list
	c = []
	for i in range(len(b)):
		d = []
		for j in range(len(b)):
			d.append(b[j][i])
		c.append(d)
	print(c)

	c = []
	for i in range(len(b)):
		d = []
		for j in range(len(b[i])):
			d.append(b[i][j] + e[i][j])
		c.append(d)
	print(c)

	c = []
	for i in range(len(b)):
		
		d1 = 0
		for j in range(len(b[i])):
			d1 += b[i][j]
		c.append(d1)

	for i in range(len(b)):
		d1 = 0
		for j in range(len(b)):
			d1 += b[j][i]
		c.append(d1)

	d2 = 0
	for i in range(len(b)):
		d2 += b[i][i]
	c.append(d2)

	d3 = 0
	for i in range(len(b)):
		d3 += b[i][len(b) - 1 - i]
	c.append(d3)

	print(c)
	v = False 
	for i in range(len(c) - 1):
		if c[i] == c[i+1]:
			continue 
		else:
			v = True 
			return("not a magic square")

	print(v)




		







main()