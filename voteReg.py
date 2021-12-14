print("Welcome to the Voter Registration App")

name = input("\nPlease enter your name: ").title().strip()
age = int(input("Please enter your age: "))

parties = ["Republican","Democratic","Independent","Libertarian","Green"] 

if age > 17:
	print("\nCongratulations "+name+"! You are old enough to register to vote.")

	print("\nHere is a list of political parties to join.")
	for party in parties:
		print("\t- "+ party)

	chosen_party = input("What party would youlike to join: ")

	if chosen_party in parties:
		print("\nCongratulation "+name+" You have joined the "+ party+" party!")
		if chosen_party =="Republican" or chosen_party == "Democratic":
			print("\nThat is major party!")
		elif chosen_party == "Independent":
			print("You are an independent person!")
		else:
			print("That is not a major party.")
	else:
		print("That is not a given party.")
else:
	print("\nYou are not old enough to register to vote.")