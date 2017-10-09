number = eval(input("Enter the number you want to count down from: ")) + 1
iteri = 0 
count = number 
while(iteri < number):
	count -= 1 
	iteri += 1 
	print(count, end = " ")
