number = eval(input("Enter numbers of your choice, when you wish to stop, enter Q: "))

count = 0 
_sum = 0 
Q = 0 

while (number != Q):
	count += 1 
	_sum += number 
	number = eval(input("Enter numbers of your choice, when you wish to stop, enter Q: "))

print(count, (_sum / count))




