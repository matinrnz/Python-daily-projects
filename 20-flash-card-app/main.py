from tkinter import *
import pandas as pd
import random
# ---------------------------- WORD GENERATOR ------------------------------- #
data = pd.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")


def next_card():
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"])


# ---------------------------- UI SETUP ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50,bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
right_image = PhotoImage(file="images/right.png")
check_button = Button(image=right_image, highlightthickness=0, command=next_card)
check_button.grid(row=1, column=1)

wrong_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

next_card()

window.mainloop()
