from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
# adding questions and answers into the question_bank
for q_a in question_data:
    question_answer = Question(q_a['text'], q_a['answer'])
    question_bank.append(question_answer)

quiz = QuizBrain(question_bank)  # quiz object

while quiz.still_has_questions():
    score = 0
    quiz.next_question()  # receives questions


print("You Have Finished The Quiz!")
print(f"Final Score: {quiz.score}/{len(question_bank)}")
