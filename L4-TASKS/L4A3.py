print("I am a Calculator")

num1s = input("input your 1st number: ")
modi = input("input your operator ( + - * / ) ")
num2s = input("input your 2nd number: ")

num1 = int(num1s) #Turning the strings to nums
num2 = int(num2s)

if modi == "+": # Addition
    print(num1, "+", num2, "=", num1 + num2)
elif modi == "-": # Subraction
    print(num1, "-", num2, "=", num1 - num2)
elif modi == "*": # Multiplication
    print(num1, "*", num2, "=", num1 * num2) 
elif modi == "/": # Division
    print(num1, "/", num2, "=", round(num1 / num2, 2))
else: # CatchAll
 print("you didnt choose a correct operator")

 