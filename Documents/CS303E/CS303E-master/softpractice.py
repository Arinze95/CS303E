class fraction:

	def __init__(self, top, bottom):
		self.num = top
		self.den = bottom

	def __str__(self):
		return(str(self.num) + "/" + str(self.den))

def main():
	myfrac = fraction(3,5)
	myfrac2 = fraction(7,8)

	print("a" + "b")
	print(myfrac)
main()