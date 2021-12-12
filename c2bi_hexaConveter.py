print("Welcome to the Binary/Hexadecimal Converter App")

max_value = int(input("Compute binary and hexadecial values up to the following decimal number: "))

#compute decimal to binary
decimal = list(range(1,max_value+1))
binary = []
hexadecimal = []

for num in decimal:
	binary.append(bin(num));
	hexadecimal.append(hex(num))

print("Generating list ... Complete")

#slice from user input
print("\nUsing slices. We will now show a portion of each list.")
lower_range = int(input("what decimal number would you like to start at: "))
upper_range = int(input("what decimal number would you like to stop at: "))

#slice
print("\nDecimal values from " + str(lower_range) + " to "+str(upper_range)+":")

for num in decimal[lower_range-1:upper_range]:
	print(num)

print("\Binary values from " + str(lower_range) + " to "+str(upper_range)+":")

for num in binary[lower_range-1:upper_range]:
	print(num)


print("\hexadecimal values from " + str(lower_range) + " to "+str(upper_range)+":")

for num in hexadecimal[lower_range-1:upper_range]:
	print(num)

#output
input("\nPress Enter to see all values from 1 to "+str(max_value)+ ".")
print("Decimal ----Binary----Hexadecimal")
print("------------------------------------------------")
for d,b,h in zip(decimal,binary, hexadecimal):
	print(str(d) + "----" + str(b)+ "----" + str(h))

