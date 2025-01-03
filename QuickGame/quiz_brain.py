class QuizBrain:
    def __init__(self,q_list):
        self.question_no=0
        self.question_list=q_list
        self.user_score=0

    def still_has_question(self):
        print(self.question_no)
        print(self.question_list)
        if self.question_no < len(self.question_list):
            return True
        else:
            return False


    def next_question(self):
        current_question =  self.question_list[self.question_no]
        self.question_no +=1
        result=input(f"Q. {self.question_no}: {current_question.text} (True/False):")
        self.check_answer(result, current_question.answer)

    def check_answer(self,u_input, correct_answer):
        if u_input.lower() == correct_answer.lower():
            print("You got it right")
            self.user_score +=1
        else:
            print("You are wrong")
        print(f"The correct answer was {correct_answer}")
        print(f"Your current score is {self.user_score}/{self.question_no}")