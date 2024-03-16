import math


x = int(input("x="))
y = int(input("y="))
r1_circle = 2


r2_circle = 1

a = math.sqrt((x-1)**2 + y**2);
b = math.sqrt((x-1)**2 + y**2);

if a <= r1_circle and b >= r2_circle:
    print("Yes", end=" ")
elif 2<=x<=6 and -5<=y<=1:
    print("Yes")
else:
    print("No", end=" ")
if x>=6 or x<=6 or y>=1 or y<=-5 :
    print("No")
