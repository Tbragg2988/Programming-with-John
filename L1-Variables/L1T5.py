print("Hello there im a basic calculator, I can calculate the average of four numbers.")

numone_s = input("Enter a first number:  ")
numtwo_s = input("Enter a second number:  ")
numthree_s = input("Enter a third number:  ")
numfour_s = input("Enter a forth number:  ")

numone = int(numone_s)
numtwo = int(numtwo_s)
numthree = int(numthree_s)
numfour = int(numfour_s)


output = (numone+numtwo+numthree+numfour)/4
print("The average of ", numone, ", ", numtwo, ", ", numthree, " and ", numfour, " is: ", output)