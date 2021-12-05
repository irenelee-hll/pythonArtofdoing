num_strings = ['15','30','40','100']
num_ints = [15,30,40,100]
num_floats = [2.2,5.0,1.245,0.142887]
num_list =[[1,2,3],[4,5,6],[7,8,9]]

print("\t\t Summary Table")

print("\nThe variable num_stings is a " + str(type(num_strings)))
print("It contains the elements: "+ str(num_strings))
print("The element " + num_strings[0] + " is a "+ str(type(num_strings[0])))

print("\nThe variable num_ints is a " + str(type(num_ints)))
print("It contains the elements: "+ str(num_ints))
print("The element " + str(num_ints[0]) + " is a "+ str(type(num_ints[0])))

print("\nThe variable num_floats is a " + str(type(num_floats)))
print("It contains the elements: "+ str(num_floats))
print("The element " + str(num_floats[0]) + " is a "+ str(type(num_floats[0])))

print("\nThe variable num_list is a " + str(type(num_list)))
print("It contains the elements: "+ str(num_list))
print("The element " + str(num_list[0]) + " is a "+ str(type(num_list[0])))

#num_strings.sort()
#num_ints.sort()
print("\nNow sorting num_strings and num_ints ...")
print("Sorted num_strings: " + str(sorted(num_strings)))
print("Sorted num_ints: " + str(sorted(num_ints)))
print("\nStrings are sorted alphabetically while integers are sorted numerically")