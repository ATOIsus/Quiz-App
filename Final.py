import random                     # To shuffle choices.
import pickle                     # To unpickle the MCQ.
from tkinter import messagebox    # To display error message.
import sqlite3                    # To connect to the database.


# region Global Variables.

question = []    # List of all questions.
anser = []       # List of all answers.

option1 = []     # List of all option.
option2 = []     # List of all option.
option3 = []     # List of all option.

score = 0        # The number of correct answers.
ques = []        # List of all MCQs (Questions and Choices).

question_no = 1  # The indexing for the question in the final program.

global quiz_topic    # The topic that is selected.

global username_var  # The username inserted during signing in.
global password_var  # The password inserted during signing in.
global PlayerID      # The ROWID of the player. (Retrieved while signing in)
global db_score      # The score in the database of the selected topic. (Retrieved while signing in)

# endregion



# region Sign In.



def signin_fun():

    """ Checks if the provided username & password is same to that stored in the database. """

    global quiz_topic
    global username_var
    global password_var
    global PlayerID
    global db_score

    try:

        username_var = input("Enter Username: ")
        password_var = input("Enter Password: ")

        conn = sqlite3.connect('Resource/2) Others/Database/Player Database.db')
        cur = conn.cursor()

        cur.execute(f"SELECT ROWID, Username, Password, {quiz_topic} FROM information")
        records = cur.fetchall()


        for record in records:

            if username_var == str(record[1]) and password_var == str(record[2]):
                PlayerID = record[0]    # ROWID
                db_score = record[3]    # quiz_topic
                print(f'PlayerID {PlayerID}')
                print(f'Db_score {db_score}')
                break
            else:
                pass
        else:
            messagebox.showerror('Error while Signing In!', 'Wrong Username or Password')

        conn.commit()
        conn.close()

    except BaseException as er:
        messagebox.showerror("Error While Signing In", str(type(er))[6:-1] + " : " + str(er))



# endregion


# region Update Function



def update_fun():
    """ Updates the score if it is greater than that stored in the database of a selected topic. """

    global db_score
    global score

    try:

        if score > db_score:

            conn1 = sqlite3.connect('Resource/2) Others/Database/Player Database.db')
            cur1 = conn1.cursor()

            cur1.execute(f"UPDATE information SET {quiz_topic} = ? where ROWID = ?", (score, PlayerID))

            conn1.commit()
            conn1.close()

            messagebox.showinfo("Congratulations!", f"{score} is your highest score!")

        else:
            pass

    except BaseException as er1:
        messagebox.showerror("Error in Update Function!", str(type(er1))[6:-1] + " : " + str(er1))

# endregion


# region Unpickle and separate MCQs.

try:
    ''' To unpickle the MCQs '''

    quiz_topic = input("Enter the file to open: ")
    file = open(f'Resource/1) Question/{quiz_topic}.txt', 'rb')

    ques = list(pickle.load(file))  # Tuple converted into list.

    random.shuffle(ques)            # Question shuffled every time teh text file is opened.

except BaseException as er2:
    messagebox.showerror("Error while database!", str(type(er2))[6:-1] + " : " + str(er2))


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

except BaseException as er3:
    messagebox.showerror("Error in separation of MCQs", str(type(er3))[6:-1] + " : " + str(er3))

# endregion


# region Displaying MCQs.


signin_fun()


def chk_ans(ans, k):

    """ Question and choices are displayed; the answer is checked and scored. """

    global score
    try:
        if choice[ans - 1] == anser[k]:  # Check if the answer is right.
            score += 1
        else:
            print()
            print(f"Wrong! The right answer was:  {anser[k]}")
            print()
    except BaseException as er4:
        messagebox.showerror("Error in chk_ans function!", str(type(er4))[6:-1] + " : " + str(er4))


try:


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
    update_fun()

except BaseException as er5:
    messagebox.showerror("Error while Displaying Questions!", str(type(er5))[6:-1] + " : " + str(er5))


# endregion