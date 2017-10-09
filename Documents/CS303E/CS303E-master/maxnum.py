numinputs = eval(input("Enter an integer (enter a 0 to stop inputs): "))
_max = numinputs
count = 1
while numinputs != 0:
	numinputs = eval(input("Enter an integer (enter a 0 to stop inputs): "))
	if numinputs > _max:
		_max = numinputs
		count = 1
	elif numinputs == _max: 
		count +=1
		
print(_max)
print(count)
