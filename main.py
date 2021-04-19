from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.title("Flashcard App")


#Cards
card_image = PhotoImage(file="./images/card_front.png")
card_canvas = Canvas(width=800, height=550, bg=BACKGROUND_COLOR, highlightthickness=0)
card_canvas.create_image(400, 275, image=card_image)
card_canvas.grid(column=0, row=0, columnspan=2)

#Labels
lan_label = Label(text="Title", font=("Arial", 40, "italic"))
lan_label.place(x=350, y=150)

word_label = Label(text="Word", font=("Arial", 50, "bold"))
word_label.place(x=325, y=263)

#Buttons
wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0)
right_button.grid(column=1, row=1)

window.mainloop()