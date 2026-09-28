print("Welcome to time conversion")

pounds = int(input("Enter an amount in pounds: £"))

seconds = pounds

if seconds < 60:
    print(str(seconds)+" seconds")
elif seconds <3600:
    print(str(round(seconds / 60, 1)) + " minutes")
elif seconds < 86400:
    print(str(round(seconds / 3600, 1))+ " hours")
elif seconds < 31536000:
    print(str(round(seconds / 86400, 1)) + " days")
else:
    print(str(round(seconds / 31536000, 1)) + " years")