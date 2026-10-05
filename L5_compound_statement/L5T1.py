print("I am a fish tank temp checker, please input your fishtanks temp and ill tell you if youre gucci")

temp = int(input("whats your temp?: ")) # input 

if temp not in [25, 26,27]: # tuple for safe temp
    if temp < 25:
        print("Too Cold get her up to 26")
    else:
        print("Too Hot, cool her down to 26")
else:
    print("thats a good temp") #confirmation of good temp