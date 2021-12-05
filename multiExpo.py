print("Welcome to the Multiplication/Exponent Table App")

name = input("Hello, What is your name: ")
num = float(input("What number would you like to work with: "))

message = name + ", Math is cool!"

print("\nMultiplication Table For "+str(num))
for x in range(1,10):
	print("\t "+ str(float(x)) +" * "+ str(num) + " = " + str(round(x*num,4)))

print("Exponent Table For "+ str(num))
for x in range(1,10):
	print("\t" + str(num)+ " ** " +str(x) +" = "+ str(round(num**x,4)))

print("\n" + message)
print("\t" + message.lower())
print("\t\t" + message.title())
print("\t\t\t" + message.upper())