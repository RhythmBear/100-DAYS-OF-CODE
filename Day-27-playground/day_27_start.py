from tkinter import *

DISPLAY_TEXT = "New Text"

window = Tk()
window.title("My first GUI Program")
window.minsize(height=500, width=500)


def button_clicked():
    global my_label, DISPLAY_TEXT
    print("I got clicked")
    DISPLAY_TEXT = "Button Clicked"
    my_label.config(text=get_input())


def new_button_clicked():
    global my_label, DISPLAY_TEXT
    print("New button got clicked")
    DISPLAY_TEXT = "BUTTON RESET"
    my_label.config(text=DISPLAY_TEXT)


def get_input():
    user = input.get()
    return user


# Label
my_label = Label(text=DISPLAY_TEXT)
my_label.config(text="New Text")
my_label.grid(column=0, row=0)

# Buttons
my_button = Button(text="click", command=button_clicked)
my_button.grid(column=1, row=1)
new_button = Button(text="reset", command=new_button_clicked)
new_button.grid(column=2, row=0)

# Entry
input = Entry(width=10)
input.grid(column=3, row=3)




window.mainloop()
