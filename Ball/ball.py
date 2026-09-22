import random


answers =[
    "Yeah I think so",
    "Nope",
    "Perhaps",
    "Man I dont know",
    "Youre kidding yourself right",
    "Of course",
    "well better you than me",
    "I wouldn't count on it",
    "I havent the foggiest idea",
    "you know, Im just a program that has a list of answers yeah?",
    "yes lad, thats it you got it buddy",
]

print("Im a magic ball ask me a question")

while True: 
    question = input("Ask me a question: ")
    if question in ["quit", "bye", "exit"]:
        print("later gater")
        break
    if question == "":
        print("Im not a mind reader, ask me a question")
        continue
    print(random.choice(answers))

    