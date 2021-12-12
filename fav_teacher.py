print("Welcome to the Favorite Teachers Program")

teachers = []
fav_teacher = input("\nWho is your first favorite teacher").title()
teachers.append(fav_teacher)
fav_teacher = input("Who is your second favorite teacher").title()
teachers.append(fav_teacher)
fav_teacher = input("Who is your third favorite teacher").title()
teachers.append(fav_teacher)
fav_teacher = input("Who is your fourth favorite teacher").title()
teachers.append(fav_teacher)

print("\nYour favorite teachers ranked are: " + str(teachers))

print("Your favorite teachers alphabetically are: "+ str(sorted(teachers)))
print("Your favorite teachers reverse alphabetically are: "+ str(sorted(teachers,reverse=True)))

print("\nYour top two teachers are: " + teachers[0] + " and " + teachers[1])
print("Your next two favorite teachers are: " + teachers[2] +" and "+ teachers[3])
print("You last favorite teacher is: " + teachers[-1])

tr_length = len(teachers)
print("You have a total of " + str(tr_length)+ "favorite teachers")


new_teacher = input("\nOops, "+ teachers[0] + " is no longer your first favorite teacher. who is your next favorite teacher: ")
teachers.insert(0, new_teacher)

print("\nYour favorite teachers ranked are: " + str(teachers))

print("Your favorite teachers alphabetically are: "+ str(sorted(teachers)))
print("Your favorite teachers reverse alphabetically are: "+ str(sorted(teachers,reverse=True)))
print("\nYour top two teachers are: " + teachers[0] + " and " + teachers[1])
print("Your next two favorite teachers are: " + teachers[2] +" and "+ teachers[3])
print("You last favorite teacher is: " + teachers[-1])

tr_length = len(teachers)
print("You have a total of " + str(tr_length)+ "favorite teachers.")


removed_tr = input("You've decided you no longer like a teacher. which teacher would you like to remove from your list: ").title()
teachers.remove(removed_tr)

print("\nYour favorite teachers ranked are: " + str(teachers))

print("Your favorite teachers alphabetically are: "+ str(sorted(teachers)))
print("Your favorite teachers reverse alphabetically are: "+ str(sorted(teachers,reverse=True)))

print("\nYour top two teachers are: " + teachers[0] + " and " + teachers[1])
print("Your next two favorite teachers are: " + teachers[2] +" and "+ teachers[3])
print("You last favorite teacher is: " + teachers[-1])

tr_length = len(teachers)
print("You have a total of " + str(tr_length)+ "favorite teachers.")
