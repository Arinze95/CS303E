_sum = 0
number = 0

while number < 20:
	number += 1  
	if number == 10 or number == 11:
		continue
	_sum += number  
print(number, end = " ")
print(_sum, end = " ")

