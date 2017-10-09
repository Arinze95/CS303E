a = ["A", "B", "C"]
b = []
def subsets (a, b, idx):
	if (idx == len(a)):
		print(b)
		return 
	else:
		c = b[:]
		b.append(a[idx])
		
		subsets(a, b, idx + 1)
		subsets(a, c, idx + 1)


def main():
	a = ["A", "B", "C"]
	b = []
	idx = int(input("Enter starting index: "))
	return subsets(a, b, idx)
main()
