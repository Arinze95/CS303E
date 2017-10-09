import math
x1, y1, x2, y2, x3, y3 = eval(input("Enter six coordinates of three points seperated by commas like x1, y1, x2, y2, x3, y3"))
a = math.sqrt(math.pow((x2-x3), 2) + math.pow((y2 - y3), 2))
b = math.sqrt(math.pow((x1-x3), 2) + math.pow((y1 - y3), 2))
c = math.sqrt(math.pow((x1-x2), 2) + math.pow((y1 - y2), 2))

A = math.degrees(math.acos((math.pow(a,2) - math.pow(b,2) - math.pow(c,2))/ (-2 * b * c)))
B = math.degrees(math.acos((math.pow(b,2) - math.pow(a,2) - math.pow(c,2))/ (-2 * a * c)))
C = math.degrees(math.acos((math.pow(c,2) - math.pow(b,2) - math.pow(a,2))/ (-2 * a * b)))

print("The three angles are ", round(A,2), round(B,2), round(C,2))

