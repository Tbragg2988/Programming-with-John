print("Hello there im a basic calculator, I can only do addition, subtraction, and multiplication right now.")

numone_s = input("Enter a first number:  ")
numtwo_s = input("Enter a second number:  ")

numone = int(numone_s)
numtwo = int(numtwo_s)

add = (numone + numtwo)
subtract = (numone - numtwo)
multiply = (numone * numtwo)

print("The calculations for outputs are:\n" "Addition: ", add,  "\n" "Subtraction: ", subtract, "\n" "Multiplication: ", multiply)