import datetime

time = datetime.datetime.now()
month= str(time.month)
day = str(time.day)
hour = str(time.hour)
minute = str(time.minute)

#welcome message
foods = ["Meat","Cheese"]
print("Welcome to the Grocery List App")
print("Current Date and Time: " + month+"/"+day+"/"+minute)
print("Your Currently have" + foods[0] + " and " + foods[1]+" in your list.")

#user input
food = input("\nType of food to the grocery list: ")
foods.append(food.title())
food = input("\nType of food to the grocery list: ")
foods.append(food.title())
food = input("\nType of food to the grocery list: ")
foods.append(food.title())


print("\nHere is your grocery list: ")
print(foods)
foods.sort()
print("here is your grocery list sorted: ")
print(foods)

print("\nSimulating grocery shopping...")
print("\nCurrent grocery list: " + str(len(foods))+ " items")
print(foods)
buy_food= input("what food did you just buy: ").title()
foods.remove(buy_food)
print("Removing " + buy_food + " from the list...")

print("\nCurrent grocery list: " + str(len(foods))+ " items")
print(foods)
buy_food= input("what food did you just buy: ").title()
foods.remove(buy_food)
print("Removing " + buy_food + " from the list...")

print("\nCurrent grocery list: " + str(len(foods))+ " items")
print(foods)
buy_food= input("what food did you just buy: ").title()
foods.remove(buy_food)
print("Removing " + buy_food + " from the list...")


#the store is out of item
print("\nCurrent grocery list: " + str(len(foods))+ " items")
print(foods)
no_item = foods.pop()
print("\n Sorry, the store is out of " + no_item+".")

new_food = input("What food would you like instead: ").title()
foods.insert(0, new_food)

print("\nHere is what remain on your grocery list:  ")
print(foods);