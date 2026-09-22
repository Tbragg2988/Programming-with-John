print("Welcome to Toms magic Month checker, wanna check a month?")

month = input("Enter the name of the month? ")
month = month.lower() # so we dont have the problem of january, January and JANUARY

# telling which season
if month in ("december", "january", "february"):
    print("This month is in Winter.")
elif month in ("march", "april", "may"):
    print("This month is in Spring.")
elif month in ("june", "july", "august"):
    print("This month is in Summer.")
elif month in ("september", "october", "november"):
    print(month, "is in autumn.")
else: 
    print("That aint a valid month champ.")

# telling which day
if month == "february":
    print("This month has 28 days (29 in a leap year)")
elif month in ("april", "june", "september", "november"):
    print("This month has 30 days")
elif month in ("january", "march", "may", "july", "august", "october", "december"):
    print("This month has 31 days")
else:
    print("you need to provide an actual calendar month: \nJanuary, February, March, April, June, July, August, September, October, November, December")