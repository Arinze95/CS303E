numelem = 5
numbers = []
sum1 = 0 

for i in range(numelem):
	value = eval(input("Enter a new number: "))
	numbers.append(value)
	sum1 += value 
print(numbers)
print(sum1)

