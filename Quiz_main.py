from Question_model import Question,QuizBrain
from Quiz_data import data

Question_bank = []
for item in data:
    Question_text = item["question"]
    Question_answer = item["answer"]
    new_question = Question(Question_text,Question_answer)
    Question_bank.append(new_question)

quiz = QuizBrain(Question_bank)
while quiz.still_questions():
    quiz.next_question()

print("quiz over!")
print(f"your score is {quiz.score}")