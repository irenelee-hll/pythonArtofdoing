print("Welcome to the Grade Sorted App")

grades = []
grade = int(input("What is your first grade (0-100): "))
grades.append(grade)
grade = int(input("What is your second grade (0-100): "))
grades.append(grade)
grade = int(input("What is your third grade (0-100): "))
grades.append(grade)
grade = int(input("What is your fourth grade (0-100): "))
grades.append(grade)

print(type(grades[0]))

print("your grades are: " + str(grades))

grades.sort(reverse=True)
print("Your grade from highest to lowest are: " + str(grades))

print("\nThe Lowest two grade will now be dropped.")
removed_grade = grades.pop()
print("Removed grade: " + str(removed_grade));

removed_grade = grades.pop()
print("Removed grade: " + str(removed_grade));

print("\nYour remaining grades are: " + str(grades))


print("Nice work! Your highest grade is " + str(max(grades)))
