print("I am a morsecode conversion")


#a dictonary of morse code reference
morse_code = {
    "a": ".-",    "b": "-...",  "c": "-.-.",  "d": "-..",   "e": ".",
    "f": "..-.",  "g": "--.",   "h": "....",  "i": "..",    "j": ".---",
    "k": "-.-",   "l": ".-..",  "m": "--",    "n": "-.",    "o": "---",
    "p": ".--.",  "q": "--.-",  "r": ".-.",   "s": "...",   "t": "-",
    "u": "..-",   "v": "...-",  "w": ".--",   "x": "-..-",  "y": "-.--",
    "z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----."
}

user_num = input("Enter one Character: ")
user_num = user_num.lower()

if user_num in morse_code:
    print("Morse code:", morse_code[user_num])
else:
    print("not part of the list")