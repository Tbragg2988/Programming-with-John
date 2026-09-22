print("Is it a workday or a weekend!?")

day = input("what day is it today? ")
day = day.lower()


if day not in ("saturday", "sunday"):
    print("Get to work!")
else:
    print("Its the weekend! 🥹")
