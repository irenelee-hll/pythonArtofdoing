name = input("What is your name: ")

sub = int(input("How many grades would you like to enter: "))
grades = []
for i in range(sub):
	score = int(input("Enter grade: "))
	grades.append(score)

print("\nGrades Highest to Lowest: ")
grades.sort(reverse=True)
sumGrade = 0
for grade in grades:
	print("\t"+str(grade))
	sumGrade+=grade

print("\n" + name+ "'s Grade Summary: ")
print("\tTotal Number of Grades: "+ str(sub))
print("\tHighest Grade: "+str(max(grades)))
print("\tLowest Grade: "+str(min(grades)))
aveNum = sumGrade/sub
print("\tAverage: " + str(aveNum))

desiredNUm = int(input("What is your desired average: "))
grade_req = desiredNUm* (len(grades)+1) -sumGrade
grade_req = round(grade_req,2)

print("Good LUck "+name+"!")
print("\nYou will need to get a "+str(grade_req) + " on your next assignment to earn a "+ str(desiredNUm)+" average")


#make a copy of original grade and swap out one of th grades
newScores = grades[:]
print("\nLets see what your average could have been if you did better/worse on an assignment.")
changedNum = int(input("What grade woul you like to change: "))
newScores.remove(changedNum)
newScores.append(int(input("What grade would you liek to change "+ str(changedNum) +" to:"))) 

#sort the new grade and print them in screen
newScores.sort(reverse=True)
print("\nNew Grades Highest to lowest: ")
for grade in newScores:
	print("\t"+ str(grade))

#cal average
new_average = sum(newScores)/len(newScores)
new_average = round(new_average,2)

print("\n" + name+ "'s New Grade Summary: ")
print("\tTotal Number of Grades: "+ str(len(newScores)))
print("\tHighest Grade: "+str(max(newScores)))
print("\tLowest Grade: "+str(min(newScores)))
print("\tAverage: " + str(new_average))

print("\nYour new average would be a "+ str(new_average)+ " compare to your real average of "+ str(aveNum)+"!")
averge_change = new_average - aveNum
averge_change = round(averge_change,2)
print("That is a change of "+ str(averge_change) + " points!")

print("\nToo bad your original grades are still the same!")
print(grades)
print("you should ask for extra credit!")
	