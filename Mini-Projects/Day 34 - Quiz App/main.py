"""
Day 34 - Quiz game entry point.
"""

from quiz_brain import QuizBrain


def main() -> int:
    """
    Main function.
    """
    quiz = QuizBrain()
    quiz.start()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
