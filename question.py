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


try:
    ''' To unpickle the MCQs '''

    file_open = input("Enter the file to open: ")
    file = open(f'Resource/1) Question/{file_open}.txt', 'rb')

    ques = list(pickle.load(file))  # Tuple converted into list.

except BaseException as er1:
    messagebox.showerror("Error", str(type(er1))[6:-1] + " : " + str(er1))


try:
    ''' Question, answer and options are separated into different lists. '''

    for i in ques:

        if len(i) == 3:  # If there are only 2 options.
            option2.append(' Both')
            option3.append(' Neither')

        elif len(i) == 4:  # If there are 3 options.
            option3.append(' None')

        for j in range(len(i)) :
            if j == 0:
                question.append(str(i[0]))
            elif j == 1:
                anser.append(str(i[1]))
            elif j == 2:
                option1.append(str(i[2]))
            elif j == 3:
                option2.append(str(i[3]))
            elif j == 4:
                option3.append(str(i[4]))

except BaseException as er2:
    messagebox.showerror("Error", str(type(er2))[6:-1] + " : " + str(er2))


try:
    ''' Question and choices are displayed; the answer is checked and scored. '''

    def chk_ans(ans, k):

        global score
        try:
            if choice[ans - 1] == anser[k]:  # Check if the answer is right.
                score += 1
            else:
                print()
                print(f"Wrong! The right answer was:  {anser[k]}")
                print()
        except BaseException as er3:
            messagebox.showerror("Error", str(type(er3))[6:-1] + " : " + str(er3))


    for l in range(len(ques)):

        choice = [anser[l], option1[l], option2[l], option3[l]]
        random.shuffle(choice)

        print()
        print(question[l])
        print()

        print('1) ' + choice[0])
        print('2) ' + choice[1])
        print('3) ' + choice[2])
        print('4) ' + choice[3])
        print()

        answer = int(input('Enter the answer number: '))

        chk_ans(answer, l)  # Function is called.

    print(f'Your score is {score} out of {len(ques)}')  # Final score.

except BaseException as er4:
    messagebox.showerror("Error", str(type(er4))[6:-1] + " : " + str(er4))
