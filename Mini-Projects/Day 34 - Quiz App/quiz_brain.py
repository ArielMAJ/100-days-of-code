"""
QuizBrain class implementation.
"""

import requests
from question_model import Question


class QuizBrain:
    """
    QuizBrain class. This handles most of the game.
    """

    def __init__(self, amount_of_questions=5):
        self.question_number = 0
        self.score = 0
        self.questions_bank = []

        self.update_questions_bank(amount_of_questions)

    def still_has_questions(self):
        """
        Checks if there are still questions left.
        """
        return self.question_number < len(self.questions_bank)

    def next_question(self):
        """
        Asks the next question.
        """
        current_question = self.questions_bank[self.question_number]
        self.question_number += 1

        print("**************************************************")
        user_answer = int(
            input(f"Q.{self.question_number}: {current_question.text} [1/0]: ")
        )
        self.check_answer(user_answer, current_question.answer)


    def check_answer(self, user_answer, actual_answer):
        """
        Checks and prints whether the answer was correct.
        """
        print("The correct answer was:", actual_answer)
        if user_answer == (actual_answer.lower() == "true"):
            print("You're right!")
            self.score += 1
        else:
            print("That's wrong")
        print(f"Your current score is {self.score}/{self.question_number}\n")

    def update_questions_bank(self, amount_of_questions) -> None:
        """
        This function will get the quiz questions online and return a list of questions
        as a Question class.
        """

        url = f"https://opentdb.com/api.php?amount={amount_of_questions}&type=boolean"
        response = requests.get(url)
        response_json = response.json()

        trivia_data = response_json["results"]

        self.questions_bank = [
            Question(text=question["question"], answer=question["correct_answer"])
            for question in trivia_data
        ]

    def start(self) -> None:
        """
        After creating the class, this function should be called to start the quiz.
        """
        while self.still_has_questions():
            self.next_question()

        print(
            "-------------------------------------------------\n"
            "You've completed the quiz!\n",
            f"Your final score is: {self.score}/{self.question_number}\n",
        )
