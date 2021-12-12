print("Welcome to the Fibonacci Calculator App")

num = int(input("\nHow many digits of the fibonacci sequence would you like to compute: "))

print("The first "+ str(num)+ "numbers of the fibonacci sequence are: ")

#compute fib
fib=[1,1]
for i in range(num-2):
	new_fib = fib[i] +fib[i+1]
	fib.append(new_fib)

print("\nThe first "+str(num)+" numbers of the fibonacci sequence are: ")

for number in fib:
	print(number)

golden=[]
for i in range(len(fib)-1):
	ratio = fib[i+1]/fib[i]
	golden.append(ratio)

print("\nThe corresponding Golden ratio values are: ")
for ratio in golden:
		print(ratio)