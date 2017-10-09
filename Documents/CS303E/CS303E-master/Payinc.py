pay = eval(input("What is your pay? "))
score = eval(input("What is your score? "))
if score > 90:
  pay = 1.03 * pay 
  print("For your efforts, your new pay is", round(pay, 3),"!")

