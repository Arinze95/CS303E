a, b = eval(input("Enter weight and price for package 1: "))
a1, b1 = eval(input("Enter weight and price for package 2: "))
priceperpound = b/a 
priceperpound1 = b1/a 
print("Package 1 has a price per pound of", priceperpound)
print("Package 2 has a price per pound of", priceperpound1)
if priceperpound < priceperpound1:
  print("Package 1 has the better price.")
if priceperpound1 < priceperpound: 
  print("Package 2 has the better price.")

