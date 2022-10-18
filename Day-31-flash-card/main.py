import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
new_word = {}
to_learn = {}
# --------------------------------------------Flipping the Card Function-----------------------------------------------#


def flip_card():
    canvas_ui.itemconfig(bg_canvas, image=back_image)
    canvas_ui.itemconfig(word_text, text=new_word['English'], fill="white")
    canvas_ui.itemconfig(title_text, text="English", fill="white")


# ----------------Reading from the french words csv file and creating new flash cards ---------------------------------#

try:
    mod_data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = mod_data.to_dict(orient="records")


def next_card():
    global new_word, flip_timer
    window.after_cancel(flip_timer)
    new_word = random.choice(to_learn)
    flip_timer = window.after(3000, func=flip_card)
    print(new_word)
    canvas_ui.itemconfig(word_text, text=new_word['French'], fill="black")
    canvas_ui.itemconfig(bg_canvas, image=card_img)
    canvas_ui.itemconfig(title_text, text="French", fill="black")


def is_known():
    to_learn.remove(new_word)
    next_card()
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)


# ------------------------------------- Creating the user interface ---------------------------------------------------#
# Creating the window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Creating the timer variable
flip_timer = window.after(3000, func=flip_card)


# Creating the canvas_ui for layering the picture and text on
canvas_ui = Canvas()
canvas_ui.config(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
back_image = PhotoImage(file="images/card_back.png")
card_img = PhotoImage(file="images/card_front.png")
bg_canvas = canvas_ui.create_image(400, 263, image=card_img)
title_text = canvas_ui.create_text(400, 120, text="French", font=TITLE_FONT)
word_text = canvas_ui.create_text(400, 263, text="Word", font=WORD_FONT)
canvas_ui.grid(column=0, row=0, columnspan=2)

# Creating the canvas_ui for the tick icon
right_img = PhotoImage(file="images/right.png")
right_canvas = Button(image=right_img, highlightthickness=0, command=is_known)
right_canvas.grid(column=1, row=1)

# Creating the canvas_ui for the wrong tick icon
wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

next_card()

window.mainloop()
