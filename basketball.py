print("Welcome to the Basketball Roster Program")

roster = []
player = input("Who is your point guard: ").title()
roster.append(player)
player = input("Who is your shooting guard: ").title()
roster.append(player)
player = input("Who is your small forward: ").title()
roster.append(player)
player = input("Who is your power forward: ").title()
roster.append(player)
player = input("Who is your center: ").title()
roster.append(player)

print("\n\t Your starting 5 from the upcoming basketball season")
print("\t\tPoint Guard:\t" + roster[0])
print("\t\tShooting Guard:\t" + roster[1])
print("\t\tShooting Guard:\t" + roster[2])
print("\t\tSmall Forward:\t" + roster[3])
print("\tCenter:\t\t"+ roster[4])


#removed player
injured_player = roster.pop(2)
print("\n Oh no," +injured_player+ " is injured." )

roster_length = len(roster)
print("Your roster only has "+ str(roster_length) + " players.")

#add a player
add_player = input("Who will take " + injured_player +" 's spot: ").title()
roster.insert(2, add_player)

#display roster
print("\n\t Your starting 5 from the upcoming basketball season")
print("\t\tPoint Guard:\t" + roster[0])
print("\t\tShooting Guard:\t" + roster[1])
print("\t\tShooting Guard:\t" + roster[2])
print("\t\tSmall Forward:\t" + roster[3])
print("\tCenter:\t\t"+ roster[4])

print("\nGood Luck "+ roster[2] + " you will do greate!")

roster_length = len(roster)
print("Your roster now has "+ str(roster_length) + " players.")

