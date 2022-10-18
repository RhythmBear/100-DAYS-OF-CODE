class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        """ Checks if the the number of questions printed has gotten to the the maximum and returns true or false"""
            return self.question_number < len(self.question_list)

    def next_question(self):
        """ Prints the next question and increases the current question number """
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} {current_question.text} (True/False): ").title()
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        """ Collects 2 arguments, the user's answer and the correct answer and compares them against each other"""
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1

        else:
            print("That's wrong! ")

        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")
