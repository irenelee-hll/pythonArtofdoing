print("Welcome to the Shipping Accounts Program")
#list of users
users = ['eramom','footea', 'davisv','admin']

name = input("\nHello, what is your name: ").lower().strip()

if(name in users):
	print("\nHello "+name+". Welcome to your account.")
	print("Current shipping prices are as follows:")

	print("\nShipping order 0 to 100:\t$5.10 each")
	print("Shipping order 100 to 500:\t$5.00 each")
	print("Shipping order 500 to 1000:\t$4.95 each")
	print("Shipping order 1000:\t\t$4.80 each")

	quantity = int(input("\nHow many items would you like to ship: "))

	#calculate
	if( quantity < 100):
		cost = 5.10
	elif quantity<500:
		cost = 5.00
	elif quantity < 1000:
		cost = 4.95
	else:
		cost= 4.88

	bill = quantity* cost
	bill = round(bill,2)

	print("To ship"+str(quantity)+ " items it will cost you $"+ str(bill)+ " at $ "+ str(cost) +" per item.")

	choice = input("\nWould you like to place this order (y/n): ").lower()
	if(choice.startswith('y')):
		print("Okay. Shopping your "+ str(quantity) + " items.")
	else:
		print("OKay. no order is being placed at this time. ")
else:
	print("Sorry, you do not have an account with us. goodbye.")