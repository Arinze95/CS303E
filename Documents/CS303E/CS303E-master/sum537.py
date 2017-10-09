import math

end = 625
i = 1 
_sum = 0 
while i < end:
	_sum = _sum + (1 / (math.sqrt(i) + math.sqrt(i + 1)))
	i += 1 

print(_sum)