import random

print("Welcome to the Coin Toss App")

print("\n I will flip a coin a set number of times.")
flip_times = int(input("how many times would you like me to flip the coin: "))

choice = input("Would you like to see the result of each flip(y/n): ").lower()
print("\nFLipping!!!\n")

head = 0
tails = 0

for flip in range(flip_times):
	coin = random.randint(0,1)
	if(coin== 1):
		head+=1
		if(choice.startswith('y')):
			print("HEADS")
	else:
		tails+=1
		if(choice.startswith('y')):
			print("TAILS")
	if head == tails:
		print("At " + str(flip+1) + " flips, the number of head and tails were equal at " + str(head)+" each.")

#calculate percentage
head_percentage= round(100*head/flip_times, 2)
tails_percentage= round(100*tails/flip_times, 2)

print("\nResults of Flipping a Coin "+ str(flip_times) + " Times: ")
print("\nSide\t\tCount\t\tPercentage")
print("Heads\t\t" + str(head) + "/" + str(flip_times)+ "\t\t" + str(head_percentage)+"%")
print("Tails\t\t" + str(tails) + "/" + str(flip_times)+ "\t\t" + str(tails_percentage)+"%")

