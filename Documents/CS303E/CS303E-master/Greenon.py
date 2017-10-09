import time 
currentTime = time. time() 
print(currentTime)
totalSeconds = int(currentTime)
print(totalSeconds)
# Get the current second
currentSecond = totalSeconds % 60
print(currentSecond)
# Get the total minutes 
totalMinutes = totalSeconds // 60
print(totalMinutes)
# Compute the current minute in the hour
currentMinute = totalMinutes % 60
print(currentMinute)
# Obtain the total hours 
totalHours = totalMinutes // 60
print(totalHours)
# Compute the current hour
currentHour = totalHours % 24
print(currentHour)
# Display results 
print("Current time is", currentHour,":",currentMinute,":",currentSecond, "GMT")
