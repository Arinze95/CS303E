x, y = eval(input("Enter a point's x and y coordinates: "))

if (0 < x < 200) and (0 < y < ((-x/2) + 100)): 
	print("The point is in the triangle")
else: 
	print("The point is not in the triangle")