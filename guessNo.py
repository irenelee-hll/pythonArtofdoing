import random

print("Welcome to the Guess My Number App")

name = input("Hello! What is your name: ").title().strip()

print("Well "+name+", I am thinkiing of a number between 1 and 20.")
number = random.randint(1,20)

for guess_num in range(5):
	guess = int(input("\nTake a guess:"))
	if(guess < number):
		print("Your guess is too low.")
	elif guess> number:
		print("Your guess is too high.")
	else:
		break

if(guess==number):
	print("\nGood job, "+name+"! You guessed my number in "+ str(guess_num+1) + " guesses!")
else:
	print("\nGame Over. The number I was thinking of was " + str(number) + ".")