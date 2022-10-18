from tkinter import *
import math


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
SECONDS = 60
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = None
mark = ""


# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global mark, REPS
    my_window.after_cancel(timer)
    # reset timer
    timer_label.config(text="Timer", fg=GREEN)
    # reset reps
    REPS = 0
    # reset marks
    mark = ""
    tick_label.config(text=mark)
    # reset timer
    my_canvas.itemconfig(text_timer, text="00:00")
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_countdown():
    global REPS
    REPS += 1
    if REPS % 2 != 0 and REPS < 8:
        count_down(WORK_MIN * SECONDS)
        timer_label.config(text="Work", fg=GREEN)

    if REPS % 2 == 0 and REPS < 8:
        count_down(SHORT_BREAK_MIN * SECONDS)
        timer_label.config(text="BREAK", fg=PINK)

    if REPS % 2 == 0 and REPS == 8:
        count_down(LONG_BREAK_MIN * SECONDS)
        timer_label.config(text="REST", fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    global REPS, mark

    # print(count)
    count_min = math.floor(count / 60)
    count_sec = count % 60
    # if count_sec == 0:
    #     count_sec = '0'

    if int(count_sec) > 9:
        my_canvas.itemconfig(text_timer, text=f"{count_min}:{count_sec}")
    else:
        my_canvas.itemconfig(text_timer, text=f"{count_min}:0{count_sec}")

    if count > 0:
        global timer
        timer = my_window.after(1000, count_down, count - 1)
    else:
        start_countdown()

        work_ses = math.floor(REPS / 2)
        for i in range(work_ses):
            mark += "✔"
        tick_label.config(text=mark, fg=GREEN)


# ---------------------------- UI SETUP ------------------------------- #
# Creating the Window

my_window = Tk()
my_window.title("Pomodoro")
my_window.config(padx=50, pady=50, bg=YELLOW)

# Creating the canvas using the canvas widget
my_canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
my_canvas.create_image(100, 112, image=tomato_img)
text_timer = my_canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

my_canvas.grid(row=1, column=1)

# Creating Labels
timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 40, "bold"), bg=YELLOW)
timer_label.grid(row=0, column=1)

tick_label = Label(font=(FONT_NAME, 8, "bold"), bg=YELLOW)
tick_label.grid(row=3, column=1)

# Creating Buttons
start_button = Button(text="Start", command=start_countdown, font=(FONT_NAME, 10))
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command=reset_timer, font=(FONT_NAME, 10))
reset_button.grid(row=2, column=2)

my_window.mainloop()
