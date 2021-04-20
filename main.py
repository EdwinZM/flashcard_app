from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
CARD_BACKGROUND = "#91C2AF"
ENGLISH_WORD = ""
try:
    french_dict = pandas.read_csv("./words_to_learn.csv").to_dict(orient="records")
except:
    french_dict = pandas.read_csv("./data/french_words.csv").to_dict(orient="records")


window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.title("Flashcard App")

#Pick a random french word from the csv using a function to add as command to the buttons
def choose_frword():
    global ENGLISH_WORD
    global french_dict
    random_word = random.choice(french_dict)
    french_word = random_word["French"]
    ENGLISH_WORD = random_word["English"]
    lan_label.config(text="French", fg="black", bg="white")
    card_canvas.itemconfig(canvas_image, image=card_image)
    word_label.config(text=french_word, fg="black", bg="white")
    window.after(3000, show_answer)

def to_learn():
    global french_dict
    new_dict = []
    for d in french_dict:
        word = d["English"]
        if word != ENGLISH_WORD:
            new_dict.append(d)
        else:
            print(word)
    french_dict = new_dict
    choose_frword()
    known_word_dict = pandas.DataFrame(french_dict)
    known_word_dict.to_csv("words_to_learn.csv", index=False)


def show_answer():
    card_canvas.itemconfig(canvas_image, image=image)
    lan_label.config(text="English", fg="white", background=CARD_BACKGROUND)
    word_label.config(text=ENGLISH_WORD, fg="white", background=CARD_BACKGROUND)

# #------------------------------UI----------------------------------

#Cards
card_image = PhotoImage(file="./images/card_front.png")
image = PhotoImage(file="./images/card_back.png")
card_canvas = Canvas(width=800, height=550, bg=BACKGROUND_COLOR, 
highlightthickness=0)
canvas_image = card_canvas.create_image(400, 275, image=card_image)
card_canvas.grid(column=0, row=0, columnspan=2)

#Labels
lan_label = Label(text="French", font=("Arial", 40, "italic"))
lan_label.place(x=400, y=150, anchor="center")

word_label = Label(text="Word", font=("Arial", 50, "bold"))
word_label.place(x=400, y=263, anchor="center")

choose_frword()

#Buttons
wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, 
command=choose_frword)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0,  command=to_learn)
right_button.grid(column=1, row=1)

window.after(3000, show_answer)
window.after_cancel(show_answer)


window.mainloop()

