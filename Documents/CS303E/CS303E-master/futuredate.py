day = eval(input("Enter an integer for today's day of the week (Sunday is 0, Monday is 1, ..., Saturday is 6: "))
elapsed = eval(input("Enter the number of days elapsed since today: "))
future = (day + elapsed) % 7 
if day == 0:
  today = "Sunday" 
if day == 1:
  today = "Monday" 
if day == 2:
  today = "Tuesday" 
if day == 3:
  today = "Wednesday" 
if day == 4:
  today = "Thursday" 
if day == 5:
  today = "Friday" 
if day == 6:
  today = "Saturday" 

if future == 0:
  fday = "Sunday" 
if future == 1:
  fday = "Monday" 
if future == 2:
  fday = "Tuesday" 
if future == 3:
  fday = "Wednesday" 
if future == 4:
  fday = "Thursday" 
if future == 5:
  fday = "Friday" 
if future == 6:
  fday = "Saturday"
print("Today is", today, "and the future day is", fday) 
