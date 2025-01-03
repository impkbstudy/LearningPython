from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]

for quest in question_data:
    q_txt = quest["question"]
    q_ans = quest["correct_answer"]
    question_bank.append(Question(q_txt,q_ans))

N_Quiz = QuizBrain(question_bank)
while N_Quiz.still_has_question:
    N_Quiz.next_question()