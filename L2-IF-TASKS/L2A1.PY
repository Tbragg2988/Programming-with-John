print("Enter a whole number and ill tell you a fact")
#enter the number for the variable
num_s = input("Whats your num?: ")
num = int(num_s)

if num >50: #asking if the number is above 50 if true it prints 
    print("Your number is over 50")
elif num < 50: #asking if the number is below 50 if true it prints
    print("Your number is under 50")
else: #if nither applys it must be 50 so it prints below
    print("The magic number is 50 well done")
