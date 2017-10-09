month = eval(input("Enter a month: "))
year = eval(input("Enter a year: "))
numberd = month % 12 

if month == 1:
  name = "January"
if month == 2:
  name - "February"
if month == 3:
  name = "March"
if month == 4:
  name = "April"
if month == 5:
  name = "May" 
if month == 6:
  name = "June" 
if month == 7:
  name = "July" 
if month == 8:
  name = "August" 
if month == 9:
  name = "September"
if month == 10:
  name = "October" 
if month == 11:
  name = "November" 
if month == 12:
  name = "December"

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
	if numberd == 1:
		day = 31 
	if numberd == 2:
		day = 29
	if numberd == 3: 
		day = 31
	if numberd == 4:
		day = 30
	if numberd == 5:
		day = 31
	if numberd == 6:
		day = 30
	if numberd == 7:
		day = 31
	if numberd == 8:
		day = 31
	if numberd == 9:
		day = 30
	if numberd == 10:
		day = 31
	if numberd == 11:
		day = 30
	if numberd == 0:
		day = 31


else: 
	if numberd == 1:
		day = 31 
	if numberd == 2:
		day = 28
	if numberd == 3: 
		day = 31
	if numberd == 4:
		day = 30
	if numberd == 5:
		day = 31
	if numberd == 6:
		day = 30
	if numberd == 7:
		day = 31
	if numberd == 8:
		day = 31
	if numberd == 9:
		day = 30
	if numberd == 10:
		day = 31
	if numberd == 11:
		day = 30
	if numberd == 0:
		day = 31

print(name, year, "has", day, "days")




