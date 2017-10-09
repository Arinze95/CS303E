import math

loanamount = eval(input("Enter loan amount: "))
numberofyears = eval(input("Enter number of years as an integer: "))



for annualinterestrate in range(5000, 8125, 125):
	monthlyinterestrate = annualinterestrate / (1200*1000)
	monthlypayment = loanamount * monthlyinterestrate / (1-1/(1+monthlyinterestrate) ** (numberofyears * 12))
	totalpayment = monthlypayment * numberofyears * 12
	print(annualinterestrate/1000, monthlypayment, totalpayment)


