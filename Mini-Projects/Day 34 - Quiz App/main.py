"""
Day 34 - Quiz game entry point.
"""

from quiz_brain import QuizBrain
from ui import MainWindow


def main() -> int:
    """
    Main function.
    """
    quiz = QuizBrain()
    # quiz.start_cmd_quiz()

    root = MainWindow(quiz)
    root.mainloop()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
