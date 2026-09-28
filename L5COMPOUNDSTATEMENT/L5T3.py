print("im truely a random machine, i only care about your fav colour and if you like the cinema or reading")

colour = input("What is your fav colour?: ") # input colour

while True: 
    cinRead = input("would you prefer going to the Cinema or reading a good book?:(answer Cinema or Reading) ").lower() # while loop to confirm you are typing in either Cinema or Reading

    if cinRead in ["cinema", "reading",]:
        break
    else:
        print("Please type either Cinema or Reading")

if colour == "blue": # blue fav colour pick either
    if cinRead == "reading":
        print("Your favourite colour is blue and you prefer to read")
    elif cinRead == "cinema":
        print("Your favourite colour is blue and you prefer the cinema")
else: # not blue is fav colour and pick either
    if cinRead == "reading":
        print("Your favourite colour is not blue and you prefer to read")
    elif cinRead == "cinema":
        print("Your favourite colour is not blue and you prefer the cinema")


# print("your fav colour is", colour, "and you prefer", cinRead) # direct path