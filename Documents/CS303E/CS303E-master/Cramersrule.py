a = eval(input("Enter a number for a: "))
b = eval(input("Enter a number for b: "))
c = eval(input("Enter a number for c: "))
d = eval(input("Enter a number for d: "))
e = eval(input("Enter a number for e: "))
f = eval(input("Enter a number for f: "))

nogood = (a * d) - (b * c)
if nogood == 0:
  print("The equation has no solution")

else:

  x = (e*d - b*f) / (a*d - b*c) 
  y = (a*f - e*c) / (a*d - b*c)
  e = (a*x) + (b*y) 
  f = (c*x) + (d*y)
  print("x is", x, "and y is", y)
  
