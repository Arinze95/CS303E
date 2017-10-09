end = 100
beg = 1
_sum = 0 
while ( beg < end):
	if beg % 15 == 0 and (0 < beg // 10 < 10):
		_sum += beg 
	beg += 1 
print(_sum)



