deposit = eval(input("Enter the monthly deposit: "))
month = 0 
accountnet = 0
monthlysavings = 0
while month < 6:
	accountnet = monthlysavings + deposit 
	monthlysavings = accountnet + (accountnet * 0.00417)
	
	month += 1 
print("After the sixth month, the account value is", monthlysavings)




