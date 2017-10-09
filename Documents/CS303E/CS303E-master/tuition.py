year = 1
tuition = 10000

for year in range(0, 10): 
	year = year + 1
	tuition = 1.05 * tuition
	tuition10 = tuition
print(tuition10) 


tuitioninitial = tuition10
year = 0
_sum = tuitioninitial
while year < 3:
	year = year + 1
	tuitioninitial = 1.05 * tuitioninitial
	_sum += tuitioninitial
print(_sum)






