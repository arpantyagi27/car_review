import math as m
x1=int(input("Enter number: "))
y1=int(input("Enter number: "))
x2=int(input("Enter number: "))
y2=int(input("Enter number: "))

distance = m.sqrt( ((x1-y2)**2)+((x2-y2)**2) )

print(distance)