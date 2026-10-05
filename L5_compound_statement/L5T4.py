print("Hello, i am a machine that asks adults if they like cars and teenagers if they like boarding")

age = int(input("Enter your age: "))


if age > 17:
    choice = input("do you like cars or motorbikes?: ")
else:
    choice = input("do you like skateboarding or cycling?: ")

print("you are", age, "and you like", choice)