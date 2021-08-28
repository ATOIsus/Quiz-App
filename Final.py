import random  # To shuffle choices.
import pickle  # To unpickle the MCQ.
import sqlite3                  # To connect to the database.
from tkinter import *           # To use basic functions and methods of tkinter.
from tkinter import messagebox  # To show popup messagebox.
from tkinter import ttk         # For the table to display the data from the database.
from PIL import Image, ImageTk  # To display images.
from playsound import playsound       # To produce sound during right, wrong answer and highest score.


# region Global Variables.

question = []  # List of all questions.
anser = []     # List of all answers.

option1 = []  # List of all option.
option2 = []  # List of all option.
option3 = []  # List of all option.

score = 0  # The number of correct answers.
ques = []  # List of all MCQs (Questions and Choices).

question_no = 1  # The indexing for the question in the final program.

global quiz_topic  # The topic that is selected.

global username_var  # The username inserted during signing in.
global password_var  # The password inserted during signing in.
global PlayerID      # The ROWID of the player. (Retrieved while signing in)
global db_score      # The score in the database of the selected topic. (Retrieved while signing in)

file_exists  = False     # Used while importing files. Is a bool value.
correct_user = False     # Used in Sign in function. Is a bool value.

global query_fun         # For Leaderboard Function.


# endregion


# region Sign In Function.



def signin_fun():
    """ Checks if the provided username & password is same to that stored in the database. """

    global quiz_topic
    global username_var
    global password_var
    global PlayerID
    global db_score
    global correct_user

    try:

        username_var = input("Enter Username: ")
        password_var = input("Enter Password: ")

        conn = sqlite3.connect('Resource/2) Others/Database/Player Database.db')
        cur = conn.cursor()

        cur.execute(f"SELECT ROWID, Username, Password, {quiz_topic} FROM information")
        records = cur.fetchall()

        correct_user = False

        for record in records:

            if username_var == str(record[1]) and password_var == str(record[2]):
                PlayerID = record[0]  # ROWID
                db_score = record[3]  # quiz_topic
                print(f'PlayerID {PlayerID}')
                print(f'Db_score {db_score}')
                correct_user = True
                messagebox.showinfo("Success", "Successfully Signed In")
                break
            else:
                pass
        else:
            messagebox.showerror('Error while Signing In!', 'Wrong Username or Password.')

        conn.commit()
        conn.close()

    except BaseException as er1:
        messagebox.showerror("Error While Signing In", str(type(er1))[6:-1] + " : " + str(er1))


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

            playsound('Resource/2) Others/Sounds/highest.wav')
            messagebox.showinfo("Congratulations!", f"{score} is your highest score!")

        else:
            pass

    except BaseException as er2:
        messagebox.showerror("Error in Update Function!", str(type(er2))[6:-1] + " : " + str(er2))


# endregion


# region Unpickle and separate MCQs.

try:
    ''' To unpickle the MCQs. '''

    quiz_topic = input("Enter the file to open: ")
    file = open(f'Resource/1) Question/{quiz_topic}.txt', 'rb')

    ques = list(pickle.load(file))  # Tuple converted into list.

    random.shuffle(ques)  # Question shuffled every time teh text file is opened.

    file_exists = True

except BaseException as er3:
    messagebox.showerror("Error with database!", str(type(er3))[6:-1] + " : " + str(er3))
    file_exists = False

try:
    ''' Question, answer and options are separated into different lists. '''

    for i in ques:

        if len(i) == 3:  # If there are only 2 options.
            option2.append(' Both')
            option3.append(' Neither')

        elif len(i) == 4:  # If there are 3 options.
            option3.append(' None')

        for j in range(len(i)):
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

except BaseException as er4:
    messagebox.showerror("Error in separation of MCQs", str(type(er4))[6:-1] + " : " + str(er4))


# endregion


# region Check Answer Function.


def chk_ans(ans, k):
    """ Question and choices are displayed; the answer is checked and scored. """

    global score
    try:
        if choice[ans - 1] == anser[k]:  # Check if the answer is right.
            playsound('Resource/2) Others/Sounds/correct.wav')
            score += 1

        else:
            playsound('Resource/2) Others/Sounds/incorrect.wav')
            print()
            print(f"Wrong! The right answer was:  {anser[k]}")
            print()
    except BaseException as er5:
        messagebox.showerror("Error in Check Answer Function!", str(type(er5))[6:-1] + " : " + str(er5))


# endregion


# region Delete Function.


try:

    def delete_fun():

        """ Deletes the row with the given ID,
            but while implementing it will delete the row of the current user only (Get ROWID in sign in function).  """


        response = messagebox.askyesno("Confirmation", "Are you sure to delete your account? ")
        Label(Tk(), text = response).grid()

        if response == 1:

            global PlayerID

            conn3 = sqlite3.connect('Resource/2) Others/Database/Player Database.db')
            c3 = conn3.cursor()

            c3.execute(f"DELETE from information WHERE ROWID = {PlayerID}")

            conn3.commit()
            conn3.close()

            messagebox.showinfo("Success!", "Account deleted!")

            query_fun()

except BaseException as er6:
    messagebox.showerror("Error while Displaying Questions!", str(type(er6))[6:-1] + " : " + str(er6))


# endregion


# region Leaderboard.



def query_fun():
    """ Shows the data of 10 users in descending order with the highest score in the selected topic. """

    # region Defining Canvas.

    root = Toplevel()
    root.title('Leaderboard')
    root.geometry('750x600')
    root.resizable(False, False)

    # endregion

    try:

        global quiz_topic

        conn = sqlite3.connect('Resource/2) Others/Database/Player Database.db')
        cur = conn.cursor()

        cur.execute(f"""SELECT ROWID, Name, Username, {quiz_topic}  FROM information 
                            ORDER BY {quiz_topic} DESC
                            LIMIT 10;""")
        rows = cur.fetchall()

        root.wm_attributes('-transparentcolor', '#AE9152')  # To make the background transparent.

        frm = LabelFrame(root, text="Leaderboard", font=('Helvetica', 34, 'bold italic'), fg="gold", labelanchor='n',
                         relief="raised", bd=15, bg='#AE9152', height=550, width=750)
        frm.grid(row=9, column=1)

        img = Image.open('Resource/2) Others/Images/lava.jpg')
        resized_img = img.resize((650, 440), Image.ANTIALIAS)
        converted_img = ImageTk.PhotoImage(resized_img)

        lbl_img = Label(frm, image=converted_img, height=440, width=650, bd=0)
        lbl_img.place(x=30, y=10)

        img1 = Image.open('Resource/2) Others/Images/lines.jpg')
        resized_img1 = img1.resize((610, 400), Image.ANTIALIAS)
        converted_img1 = ImageTk.PhotoImage(resized_img1)

        lbl_img1 = Label(lbl_img, image=converted_img1, height=400, width=610, bd=0)
        lbl_img1.place(x=23, y=25)

        style = ttk.Style()  # Styling the table.
        style.theme_use("clam")
        style.configure("Treeview",
                        rowheight=30,
                        background="black",
                        foreground="#FFD700",
                        font=('Helvetica', 14, 'bold italic'))
        style.map('Treeview', background=[('selected', 'Black')], foreground=[('selected', 'red')])

        style.configure("Treeview.Heading", background="black", foreground="gold", font=('Helvetica', 14, 'bold italic'))
        style.map('Treeview.Heading', background=[('selected', 'red')])

        tv = ttk.Treeview(lbl_img1, column=(1, 2, 3, 4), show="headings", height=10)  # The table.
        tv.place(x=13, y=33)

        tv.column(1, width=50, stretch=False)
        tv.column(2, width=190, stretch=False)
        tv.column(3, width=205, stretch=False)
        tv.column(4, width=135, stretch=False)

        tv.heading(1, text="ID")
        tv.heading(2, text="Name")
        tv.heading(3, text="Username")
        tv.heading(4, text=f"{quiz_topic}")

        for o in rows:
            tv.insert("", "end", values=o)

        conn.commit()
        conn.close()

        delete_btn = Button(root, text="Delete", command=delete_fun)
        delete_btn.grid(row=12, column=0, columnspan=2, pady=10, padx=10, ipadx=120)

    except BaseException as er7:
        messagebox.showerror("Error in Query Function!", str(type(er7))[6:-1] + " : " + str(er7))

    else:
        root.mainloop()


# endregion


# region Displaying MCQs.


if file_exists:

    signin_fun()  # Calling Sign In function.

else:
    messagebox.showerror("Error while loading file!", "File not found.")


if correct_user:  # If correct username and password is given, correct_user = True.

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

            chk_ans(answer, l)  # Check Answer Function is called.

            question_no += 1

        print(f'Your score is {score} out of {len(ques)}')  # Final score.

        update_fun()  # Calling the Update Function.


        query_fun()  # Calling the leaderboard Function.

    except BaseException as er8:
        messagebox.showerror("Error while Displaying Questions!", str(type(er8))[6:-1] + " : " + str(er8))

else:
    messagebox.showerror("Error in Sign in!", "You can't take the quiz.")


# endregion