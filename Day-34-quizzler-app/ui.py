from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=50, bg=THEME_COLOR)
        self.font = FONT
        self.bg_color = THEME_COLOR

        # Creating the buttons
        # TRUE BUTTON
        self.true_img = PhotoImage(file="images/true.png")
        self.tick_button = Button(image=self.true_img, highlightthickness=0, command=self.tick_button)
        self.tick_button.grid(row=2, column=0, padx=20, pady=20)

        # FALSE BUTTON
        self.false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_img, highlightthickness=0, command=self.wrong_button)
        self.false_button.grid(row=2, column=1, padx=20, pady=20 )

        # Creating the canvas for the text
        self.canvas = Canvas()
        self.canvas.config(width=300, height=250, highlightthickness=0, bg='white')
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=280,
                                                     text="Question Goes here",
                                                     font=FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=40)

        # Creating the Score text
        self.scoreboard = Label(text=f"SCORE : {self.quiz.score}",
                                fg="white",
                                font=(14),
                                bg=THEME_COLOR,
                                padx=10,
                                pady=10)
        self.scoreboard.grid(row=0, column=1,)
        # Calling the function to get the next question so that it appears when we run our code
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        # Checks to see if there are still questions before updating
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():

            self.scoreboard.config(text=f"SCORE : {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            # they have come to the end of the quiz
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.question_text,
                                   text=f"You have come to the end. Your final score is {self.quiz.score}/{10}")
            self.tick_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def tick_button(self, answer="True"):
        remark = self.quiz.check_answer(answer)
        self.give_feedback(remark)

    def wrong_button(self, answer="False"):
        remark = self.quiz.check_answer(answer)
        self.give_feedback(remark)

    def give_feedback(self, remark):
        if remark:
            self.canvas.config(bg="green")
            # Update their score of they get it right
            self.quiz.score += 1

        else:
            self.canvas.config(bg="red")

        self.window.after(2000, func=self.get_next_question)

    def update_score(self):
        self.scoreboard.config(text=f"SCORE : {self.quiz.score}")

# test_interface = QuizInterface()