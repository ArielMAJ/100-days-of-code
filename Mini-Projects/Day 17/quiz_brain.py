class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1

        user_answer = int(input(f"Q.{self.question_number}: {current_question.text} [1/0]: "))
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, actual_answer):
        print("The correct answer was:", actual_answer)
        if user_answer == (actual_answer.lower() == 'true'):
            print("You're right!")
            self.score += 1
        else:
            print("That's wrong")
        print(f"Your current score is {self.score}/{self.question_number}\n")
