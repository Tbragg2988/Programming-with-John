import tkinter as tk
import random
from tkinter import *
from PIL import Image, ImageTk



#answers now with the correct ratio 2:1:1 total of 20 answers d20*
answers = [
    # Positive (10)
    "Of course",
    "Yes lad, thats it you got it buddy",
    "Yeah I think so",
    "Oh definitely, no doubt about it",
    "You bet your life on it",
    "It's looking good from here",
    "Reckon so, yeah",
    "As sure as the sun comes up",
    "Too right, go for it",
    "Signs are all pointing yes mate",

    # Neutral (5)
    "Perhaps",
    "Man I dont know",
    "I havent the foggiest idea",
    "You know, Im just a program that has a list of answers yeah?",
    "Ask me again in a bit, yeah?",

    # Negative (5)
    "Nope",
    "You're kidding yourself right",
    "I wouldn't count on it",
    "Well better you than me",
    "Not a chance, mate",
]
# when ask button pushed it actives and chooses an item from list or replys with the blank screen message
def get_answer(event=None): 
    question = entry.get()
    if question.strip() == "":
        result_label.config(text="I'm not a mind reader, please ask a question.")
        return
    result_label.config(text=random.choice(answers))
    entry.delete(0, tk.END)

    


# the created window of the "exe" file
root= tk.Tk()
root.title("Magic 8 Ball")

window_height = 500
window_width = 500
screen_width = root.winfo_screenwidth()   #asking windows itself what size is the screen
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width/2) 
center_y = int(screen_height/2 - window_height/2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}') # Telling the new window to open in the center of the screen (info found out by previous command)
root.resizable(False, False)
root.iconbitmap("Ball/assets/isoball.ico")
#background_image=tk.PhotoImage(file="Ball/assets/eight_ball_bg.png")

#bg= PhotoImage(file = "Ball/assets/eight_ball_bg.png") leaving this here as redundant code 

pil_image = Image.open("Ball/assets/eight_ball_bg.png") # pillow program reshaping background image
pil_image = pil_image.resize((500, 400))
bg = ImageTk.PhotoImage(pil_image)


label1 = Label(root, image = bg) # applying backgroun to the code
label1.place(anchor="center", relx=0.5, rely=0.5, width=500, height=400)


# Place a label on the root window
message = tk.Label(
    root,
    text="Im a Magic 8 ball ask me weird questions!", 
    font=("Georgia", 13, "bold"),
    bg="white",
    fg="#222222"
    )

message.place(relx=0.5, rely=0.1, anchor="center")

entry = tk.Entry(
    root,
    width=30,
    font=("Georgia", 11),
    relief="solid",
    borderwidth=1,
    justify="center"
)
entry.place(relx=0.5, rely=0.22, anchor="center")
entry.bind("<Return>", get_answer)
                            
result_label = tk.Label(root,  
                        text="", 
                        wraplength=300, 
                        font=("Arial", 11),
                        relief="solid",
                        borderwidth=2,
                        bg="white"
                        )
result_label.place(relx=0.5, rely=0.5, anchor="center")

root.mainloop()