print("i am the exam monster i will tell you what grade your grade is comparable too")

grade = input("What is your grade? ") # input for grade 

if grade.isnumeric(): # checker to make sure words arnt be put in.
    grade = int(grade)
    if grade < 20:
        print("Grade U, try harder bruddah.")
    elif grade >= 20 and grade < 30:
        print("Grade E, yikes ")
    elif grade >= 30 and grade < 46:
        print("Grade D, If you plug in the keyboard maybe do better.")
    elif grade >= 46 and grade < 60:
        print("Grade C, at least you turned the monitor on. ")
    elif grade >= 60 and grade < 76:
        print("Grade B, respectable")
    elif grade >= 76 and grade < 90:
        print("Grade A, gratz huge achieve. ")
    else:
        print("Grade A*, mans showing off")

else:
    print("You did not enter a valid number my guy.") # failing validation of numeric checker