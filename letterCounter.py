print(" Welcome to the Letter Counter App");

first_name = input("What is your name: ").title().strip()

print("Hello "+ first_name+"!");

print("I will count the number of times that a specific letter occurs in a message.")
message = input("Please enter a message: ")
letter = input("Which letter would you like to count the occurences of: ")

message = message.lower()
letter = letter.lower()

letter_count = message.count(letter);

print(first_name + ", your message has " +str(letter_count)+" "+str(letter)+ "'s in it")