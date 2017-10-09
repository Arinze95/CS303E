year = 0
tuition = 10000
while tuition / 10000 < 2:
	year += 1 
	tuition = 1.07 * tuition 
print("Tuition will be doubled in year", year, "and will be an outstanding", tuition)

