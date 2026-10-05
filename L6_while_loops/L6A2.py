print("Type in a number and ill keep a running total of all")

count = 0
total = 0
msg = ""

while True:
    num_s = input("Enter a number (e to exit)>>>")
    if num_s == "e":
            break

    num = int(num_s)
    total = total + num
    count += 1
    msg += num_s + " + "
    
msg = msg[:-1]

print(f"you typed in {count} numbers")
print(f"The total is {total}")
print(msg + "= " + str(total))
print("Bye!!")
