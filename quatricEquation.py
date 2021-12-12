import cmath

print("Welcome to the Quadratic Solver App");

print("\nA quadratic equation is of the form ax^2 +bx +c = 0");
print("Your solution can be real or complex numbers.")
print("A complex number has two parts: a+ bj");
print("Where a is the real protion and bj is the imaginary portion.")

equationTimes = int(input("\nHow many equation would you like to solve today: "))

for i in range(equationTimes):
	print("\nSolving equation #"+str(i+1))
	print("------------------------------")
	a = float(input("\nPlease enter your value of a coefficient of x^2):"))
	b = float(input("\nPlease enter your value of a coefficient of x):"))
	c = float(input("\nPlease enter your value of a coefficient):"))


	#solving the quadratic formula
	x1 = (-b + cmath.sqrt(b**2 - 4*a*c))/(2*a)
	x2 = (-b - cmath.sqrt(b**2 - 4*a*c))/(2*a)
	print("\nThe solution to "+str(a)+"x^2 + " +str(b)+"x + "+str(c)+" are: ")

	print("\n\tx1 = " + str(x1))
	print("\tx2 = " + str(x2))

print("\nThank you for using the Quadratic Equation solver App.goodbye")

