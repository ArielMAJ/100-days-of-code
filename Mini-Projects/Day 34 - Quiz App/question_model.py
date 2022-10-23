"""
Question class implementation.
"""

import html


class Question:
    """
    Question class.
    """

    def __init__(self, text, answer):
        self.text: str = text
        self.answer: str = answer

    @property
    def text(self):
        """
        Text property. Works about the same as a "normal" variable, but the setter ensures
        html will always be unescaped.
        """
        return self._text

    @text.setter
    def text(self, text):
        self._text = html.unescape(text)

    @property
    def answer(self):
        """
        Answer property. Works about the same as a "normal" variable, but the setter ensures
        html will always be unescaped.
        """
        return self._answer

    @answer.setter
    def answer(self, answer):
        self._answer = html.unescape(answer)
