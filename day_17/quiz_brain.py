# TODO: asking the questions
# TODO: checking if the answer was correct
# TODO: checking if we're the end of the quiz


class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        choice = input(f"Q.{self.question_number} {current_question.text} (True/False?) ")
        self.check_answer(choice, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Correct Answer")
            self.score += 1
        else:
            print("Wrong Answer")
        print(f"The Correct Answer was: {correct_answer}")
        print(f"Score: {self.score}/{self.question_number}")
        return self.score


