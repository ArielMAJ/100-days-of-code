from question_model import Question
# from data import question_data
from quiz_brain import QuizBrain
import requests


amount_of_questions = 5
# difficulty = 'easy'
# url = f'https://opentdb.com/api.php?amount={amount_of_questions}&category=18&difficulty={difficulty}&type=boolean'


# url= "https://opentdb.com/api_token.php?command=request" # Use this to get tokens
# r = requests.get(url)
 #,headers=headers,data=data)

url = f'https://opentdb.com/api.php?amount={amount_of_questions}&type=boolean'
response = requests.get(url)
response_json = response.json()


if response_json['response_code']!=0:
    reset_url = f"https://opentdb.com/api_token.php?command=reset"
    new_response = requests.get(reset_url)
    print(new_response,new_response.text)
    response_json = requests.get(url).json()

question_data = response_json['results']

# with open("opentdb.py",'w') as data_py:  #Write data to a file.
#     data_py.write(f"question_data = {r.json()['results']}")


# question_bank = [Question(*question.values()) for question in question_data]
question_bank = [Question(text=question['question'], answer=question['correct_answer']) for question in question_data]

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz!\nYour final score is: {quiz.score}/{quiz.question_number}")