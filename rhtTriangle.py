import math

print("Welcome to the Right Triangle Solver App")

side_a = float(input("What is the first leg of the triangle: "))
side_b = float(input("What is the second leg of the triangle: "))

#calculate right triangle or not
side_c = math.sqrt(side_a**2 + side_b**2);
side_c = round(side_c,3)

area = 0.5* side_a*side_b
area = round(area,3)

print("For a triangle with legs of "+str(side_a)+ " and "+ str(side_b)+" the hypotenuse is "+ str(side_c));
print("For a triangle with legs of "+str(side_a)+ " and "+ str(side_b)+" the area is "+ str(area));

