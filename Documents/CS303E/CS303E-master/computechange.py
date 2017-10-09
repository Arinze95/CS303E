amount = eval(input("Enter an amount, for example, 11.56: "))

remainingamount = int(amount*100)

numberof1dollars = remainingamount // 100
remainingamount = remainingamount % 100

numberofquarters = remainingamount // 25 
remainingamount = remainingamount % 25

numberofdimes = remainingamount // 10
remainingamount = remainingamount % 10

numberofnickels = remainingamount // 5
remainingamount = remainingamount % 5

numberofpennies = remainingamount

print("Your amount", amount, "consists of\n", "\t", numberof1dollars, "dollars\n", 
"\t", numberofquarters, "quarters\n", "\t", numberofdimes, "dimes\n", "\t", numberofnickels, "nickels\n", "\t", numberofpennies, "pennies")

