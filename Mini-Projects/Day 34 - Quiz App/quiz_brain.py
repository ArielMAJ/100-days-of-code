"""
QuizBrain class implementation.
"""

import requests
from question_model import Question


class QuizBrain:
    """
    QuizBrain class. This handles most of the game.
    """

    def __init__(self, amount_of_questions: int = 5):
        self.question_number: int = 0
        self.score: int = 0
        self.questions_bank: list[Question]
        self.current_question: Question

        self.update_questions_bank(amount_of_questions)

    def still_has_questions(self) -> bool:
        """
        Checks if there are still questions left.
        """
        return self.question_number < len(self.questions_bank)

    def next_question(self) -> None:
        """
        "Prepares" the next question.
        """
        self.current_question = self.questions_bank[self.question_number]
        self.question_number += 1

    def ask_next_question_cmd(self) -> None:
        """
        Asks the next question on cmd.
        """
        self.next_question()

        print("**************************************************")
        user_answer: int = int(
            input(f"Q.{self.question_number}: {self.current_question.text} [1/0]: ")
        )
        self.check_answer_cmd(user_answer)

    def answer_is_correct(self, user_answer: int) -> bool:
        """
        Checks whether the answer was correct.
        """
        if user_answer == (self.current_question.answer.lower() == "true"):
            self.score += 1
            return True
        return False

    def check_answer_cmd(self, user_answer: int) -> None:
        """
        Checks and prints whether the answer was correct.
        """
        print("The correct answer was:", self.current_question.answer)
        if self.answer_is_correct(user_answer):
            print("You're right!")
        else:
            print("That's wrong")
        print(f"Your current score is {self.score}/{self.question_number}\n")

    def update_questions_bank(self, amount_of_questions: int) -> None:
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

    def start_cmd_quiz(self) -> None:
        """
        After creating the class, this function should be called to start the quiz.
        """
        while self.still_has_questions():
            self.ask_next_question_cmd()

        print(
            "-------------------------------------------------\n"
            "You've completed the quiz!\n",
            f"Your final score is: {self.score}/{self.question_number}\n",
        )
