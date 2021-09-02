import random  # To shuffle choices.
import pickle  # To unpickle the MCQ.
from tkinter import messagebox  # To display error message.


question = []  # List of all questions.
anser = []     # List of all answers.
option1 = []   # List of all option.
option2 = []   # List of all option.
option3 = []   # List of all option.
score = 0      # The number of correct answers.
ques = []      # List of all MCQs.
question_no = 1  # The indexing for the question in the final program.





def chk_ans(ans, k):

    global score
    global choice
    global  question_no


    if choice[ans - 1] == anser[k]:  # Check if the answer is right.
        score += 1
    else:
        print()
        print(f"Wrong! The right answer was:  {anser[k]}")
        print()


for l in range(len(ques)):


    choice = [anser[l], option1[l], option2[l], option3[l]]
    random.shuffle(choice)

    print()
    print(f'{question_no})  {question[l]}')
    print()

    print('1) ' + choice[0])
    print('2) ' + choice[1])
    print('3) ' + choice[2])
    print('4) ' + choice[3])
    print()

    answer = int(input('Enter the answer number: '))

    chk_ans(answer, l)  # Function is called.

    question_no += 1

print(f'Your score is {score} out of {len(ques)}')  # Final score.
