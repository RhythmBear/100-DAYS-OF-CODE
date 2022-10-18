from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for dictionary in question_data:
    new_question = Question(dictionary['text'], dictionary['answer'])
    question_bank.append(new_question)



quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've succesfully completed the game")
print(f"Your final score is {quiz.score} / {len(quiz.question_list)}")

