import random  # To shuffle choices.
import pickle  # To unpickle the MCQ.
from tkinter import *              # To use basic functions and methods of tkinter.
from tkinter import messagebox     # To show popup messagebox.
from playsound import playsound    # To produce sound during right, wrong answer and highest score.
from tkinter import ttk            # For the table to display the data from the database.
import sqlite3                     # To use database.



# region Global Variables.

question = []  # List of all questions.
anser = []     # List of all answers.

option1 = []  # List of all option.
option2 = []  # List of all option.
option3 = []  # List of all option.

score = 0  # The number of correct answers.
ques = []  # List of all MCQs (Questions and Choices).

global choice            # For Check Function.

ques_index = 1           # To Count the number of questions.

global choice_var        # IntVar used in Selected Function.
global quiz_topic        # The topic chosen in Start Function.


global img3, img4, img5, img6, img7, img8, img9, img10   # To display the images in start function.
global labelQuestion1, r1, r2, r3, r4                    # To display questions and options.

global ent_uname_in, ent_pass_in                                # For Sign In Function.
global player_ID, db_score                                      # For Sign In Function.
global ent_uname_up, ent_email_up, ent_pass_up, ent_c_pass_up   # For Sign Up Function.



# endregion




# region 7) Leaderboard (Sabin).



def query_fun():
    """ Shows the data of 10 users in descending order with the highest score of the selected topic. """

    global quiz_topic

    leaderboard_label.grid()

    conn1 = sqlite3.connect('Resource/2) Others/Database/Player Database.db')
    cur1 = conn1.cursor()

    cur1.execute(f"""SELECT ROWID, Name, Username, {quiz_topic}  FROM information 
                        ORDER BY {quiz_topic} DESC
                        LIMIT 10;""")
    rows = cur1.fetchall()

    frm = LabelFrame(leaderboard_label, text="Leaderboard", font=('Helvetica', 34, 'bold italic'), fg="gold", labelanchor='n',
                     relief="raised", bd=15, bg='#AE9152', height=550, width=750)
    frm.grid(row=9, column=1)


    image_1 = PhotoImage(file="Resource/2) Others/Images/lava.png")

    lbl_image = Label(frm, image=image_1, height=440, width=650, bd=0, bg = "Gold")
    lbl_image.place(x=30, y=10)

    image_2 = PhotoImage(file="Resource/2) Others/Images/lines.png")

    lbl_image1 = Label(lbl_image, image=image_2, height=400, width=610, bd=0, bg = "Black")
    lbl_image1.place(x=23, y=25)

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

    tv = ttk.Treeview(lbl_image1, column=(1, 2, 3, 4), show="headings", height=10)  # The table.
    tv.place(x=9, y=30)

    tv.column(1, width=50, stretch=False)
    tv.column(2, width=190, stretch=False)
    tv.column(3, width=205, stretch=False)
    tv.column(4, width=145, stretch=False)

    tv.heading(1, text="ID")
    tv.heading(2, text="Name")
    tv.heading(3, text="Username")
    tv.heading(4, text=f"{quiz_topic}")

    for o in rows:
        tv.insert("", "end", values=o)

    conn1.commit()
    conn1.close()

    delete_btn = Button(leaderboard_label, text="Delete")  # , command=delete_fun)
    delete_btn.grid(row=12, column=0, columnspan=2, pady=10, padx=10, ipadx=120)


# endregion




# region 6) Selected Function (Abhinav).



def selected_fun():
    """ Loads/passes next question and choices to the question_fun """

    global ques_index
    global labelQuestion1, r1, r2, r3, r4
    global choice
    global score


    choice_var.set(-1)


    if ques_index == 21:
        question_label.destroy()
        query_fun()


    elif ques_index < 21:
        choice = [anser[ques_index-1], option1[ques_index-1], option2[ques_index-1], option3[ques_index-1]]
        random.shuffle(choice)

        labelQuestion1.config(text=f" {ques_index}) {question[ques_index-1]}")
        r1['text'] = choice[0]
        r2['text'] = choice[1]
        r3['text'] = choice[2]
        r4['text'] = choice[3]

        ques_index += 1

    else:
        pass


# endregion



# region 5) Check Answer Function (Sabin).



def chk_ans(ans, k):
    """ The choice is checked and scored accordingly. """

    global score
    global choice
    global ques_index

    try:
        if choice[ans] == anser[k-2]:  # Check if the answer is right.
            playsound('Resource/2) Others/Sounds/correct.wav')
            score += 1

        else:
            playsound('Resource/2) Others/Sounds/incorrect.wav')


        if ques_index < 22:
            selected_fun()

        else:
            pass

    except BaseException as er5:
        messagebox.showerror("Error in Check Answer Function!", str(type(er5))[6:-1] + " : " + str(er5))


# endregion



# region 4) Displaying MCQs (Abhinav).



def question_fun():
    """ To display the question and choices of the selected topic. """

    topic_label.destroy()
    frame_signin.destroy()

    global labelQuestion1, r1, r2, r3, r4
    global ques_index
    global choice_var


    question_label.grid(padx = 100, pady = 120)

    labelQuestion1 = Label(question_label, font=("Berlin Sans FB", 17), background="#66b3ff", wraplength=620, justify = "left")
    labelQuestion1.place(x = 5, y = 50)

    choice_var = IntVar()
    choice_var.set(-1)


    r1 = Radiobutton(question_label, font=("Times", 15),  bg="#66b3ff", variable = choice_var,  justify = "left", value = 0, command= lambda : chk_ans(0, ques_index))
    r1.place(x = 5, y = 165)

    r2 = Radiobutton(question_label, font=("Times", 15), bg="#66b3ff", variable = choice_var, justify = "left", value = 1, command= lambda : chk_ans(1, ques_index))
    r2.place(x = 5, y = 205)

    r3 = Radiobutton(question_label, font=("Times", 15), bg="#66b3ff", variable = choice_var, justify = "left", value = 2, command= lambda : chk_ans(2, ques_index))
    r3.place(x = 5, y = 245)

    r4 = Radiobutton(question_label, font=("Times", 15), bg="#66b3ff", variable = choice_var, justify = "left", value = 3, command= lambda : chk_ans(3, ques_index))
    r4.place(x = 5, y = 285)

    if ques_index < 22:
        selected_fun()
    else:
        pass



# endregion



# region 7) Sign Up to Database (Sabin & Bishal).



def sign_up():

    global ent_uname_up, ent_email_up, ent_pass_up, ent_c_pass_up

    if ent_uname_up.get() == '' and ent_pass_up.get() == '' and ent_email_up.get() == '' and ent_c_pass_up.get() == '':
        messagebox.showerror("Error!", "Cannot Enter Empty Fields!")

    elif ent_email_up.get() == '':
        messagebox.showerror("Error!", "Cannot Enter Empty Email!")

    elif ent_uname_up.get() == '':
        messagebox.showerror("Error!", "Cannot Enter Empty Username!")

    elif ent_pass_up.get() == '':
        messagebox.showerror("Error!", "Cannot Enter Empty Password!")

    elif ent_c_pass_up.get() == '':
        messagebox.showerror("Error!", "Cannot Enter Empty Confirm Password!")

    elif ent_pass_up.get() != ent_c_pass_up.get():
        messagebox.showerror("Error!", "Password and Confirm Password need to be the same!")

    else:
        conn1 = sqlite3.connect('Resource/2) Others/Database/Player Database.db')
        c1 = conn1.cursor()

        c1.execute(f"SELECT Username FROM information")
        records = c1.fetchall()

        for record in records:

            if ent_uname_up.get() == str(record[0]):
                messagebox.showerror("Error!", "Cannot Use Same Username Twice!")
                break

            else:
                pass

        else:
            c1.execute(
                """INSERT INTO information VALUES (:Email, :Username, :Password, :Architecture, 
                :Lab , :Math , :Politics , :Programming , :Science , :Sport, :GK)""",
                {
                    'Email': ent_email_up.get(),
                    'Username': ent_uname_up.get(),
                    'Password': ent_pass_up.get(),
                    'Architecture': 0,
                    'Lab': 0,
                    'Math': 0,
                    'Politics': 0,
                    'Programming': 0,
                    'Science': 0,
                    'Sport': 0,
                    'GK': 0,
                })

            messagebox.showinfo("Completed", "Player Data Inserted")

        conn1.commit()
        conn1.close()

        ent_uname_up.delete(0, END)
        ent_email_up.delete(0, END)
        ent_pass_up.delete(0, END)
        ent_c_pass_up.delete(0, END)

        sign_in_GUI()


# endregion



# region 6) Sign Up (Bishal).




def sign_up_GUI():

    global ent_uname_up, ent_email_up, ent_pass_up, ent_c_pass_up
    global frame_signup

    frame_signin.destroy()

    frame_signup = LabelFrame(root_main, bg="white", bd=0, height=400, width=450)
    frame_signup.place(x=150, y=110)


    lbl_signup = Label(frame_signup, text="Sign Up", font=("Times", 30, "bold"), fg="green", bg="white")
    lbl_signup.place(x=60, y=5)

    lbl_u_name = Label(frame_signup, text="Username", font=("arial", 15, "bold"), fg="green", bg="white")
    lbl_u_name.place(x=60, y=53)
    ent_uname_up = Entry(frame_signup, font="arial,15", bg="light green")
    ent_uname_up.place(x=60, y=80, width="300", height="30")

    lbl_email = Label(frame_signup, text="E-mail", font=("arial", 15, "bold"), fg="green", bg="white")
    lbl_email.place(x=60, y=110)
    ent_email_up = Entry(frame_signup, font="arial,15", bg="light green")
    ent_email_up.place(x=60, y=140, width="300", height="30")

    lbl_pass = Label(frame_signup, text="Password", font=("arial", 15, "bold"), fg="green", bg="white")
    lbl_pass.place(x=60, y=170)
    ent_pass_up = Entry(frame_signup, font="arial,15", bg="light green", show="*")
    ent_pass_up.place(x=60, y=200, width="300", height="30")

    lbl_c_pass = Label(frame_signup, text="Confirm Password", font=("arial", 15, "bold"), fg="green", bg="white")
    lbl_c_pass.place(x=60, y=230)
    ent_c_pass_up = Entry(frame_signup, font="arial,15", bg="light green", show="*")
    ent_c_pass_up.place(x=60, y=260, width="300", height="30")

    btn_signup_up = Button(frame_signup, text="Sign Up", bd=3, bg="green", fg="white", font=("arial", 15), command=sign_up)
    btn_signup_up.place(x=160, y=310)

    btn_signin_up = Button(frame_signup, text="SIGN IN", bd=4, bg="blue", fg="white", font=("arial", 15), command=sign_in_GUI)
    btn_signin_up.place(x=350, y=350)


# endregion



# region 5) Check Sign In Details (Sabin & Bishal).



def sign_in():

    global ent_uname_in, ent_uname_in
    global quiz_topic, player_ID, db_score


    if ent_uname_in.get() == "" or ent_pass_in.get() == "":
        messagebox.showerror("Error", "All fields are required")

    else:

        conn2 = sqlite3.connect('Resource/2) Others/Database/Player Database.db')
        cur2 = conn2.cursor()

        cur2.execute(f"SELECT ROWID, Username, Password, {quiz_topic} FROM information")
        records = cur2.fetchall()


        for record in records:

            if ent_uname_in == str(record[1]) and ent_pass_in == str(record[2]):
                player_ID = record[0]  # ROWID
                db_score = record[3]  # quiz_topic

                messagebox.showinfo("Success", "Successfully Signed In")

                ent_uname_in.delete(0, END)
                ent_pass_in.delete(0, END)

                break
            else:
                pass
        else:
            messagebox.showerror('Error while Signing In!', 'Wrong Username or Password.')

        conn2.commit()
        conn2.close()

        start_fun()


# endregion



# region 4) Sign In GUI (Bishal).



def sign_in_GUI():

    frame_signup.destroy()
    topic_label.destroy()

    global ent_uname_in, ent_pass_in
    global frame_signin

    frame_signin = LabelFrame(root_main, bg="white", bd=0, height=400, width=450)
    frame_signin.place(x=150, y=110)

    lbl_signin = Label(frame_signin, text="Sign In", font=("Times", 30, "bold"), fg="green", bg="white")
    lbl_signin.place(x=60, y=30)

    lbl_user_n = Label(frame_signin, text="Username", font=("arial", 15, "bold"), fg="green", bg="white")
    lbl_user_n.place(x=60, y=90)
    ent_uname_in = Entry(frame_signin, font="arial, 15", bg="light green")
    ent_uname_in.place(x=60, y=120, width="300", height="30")

    lbl_p_word = Label(frame_signin, text="Password", font=("arial", 15, "bold"), fg="green", bg="white")
    lbl_p_word.place(x=60, y=160)
    ent_pass_in = Entry(frame_signin, font="arial, 15", bg="light green", show="*")
    ent_pass_in.place(x=60, y=190, width="300", height="30")

    btn_signin_in = Button(frame_signin, text="Sign In", bd=4, bg="green", fg="white", font=("arial", 15), command=sign_in)
    btn_signin_in.place(x=160, y=240)

    btn_signup_in = Button(frame_signin, text="SIGN UP", bd=4, bg="blue", fg="white", font=("arial", 15), command=sign_up_GUI)
    btn_signup_in.place(x=345, y=350)


#  endregion



# region 3) Unpickle and Separate MCQs (Sabin).



def unpickle_fun(quiz_topic_pa):
    """ To unpickle the MCQs and separate question, answer and choices."""

    global ques
    global quiz_topic

    quiz_topic = quiz_topic_pa

    try:
        ''' To unpickle the MCQs. '''


        file = open(f'Resource/1) Question/{quiz_topic_pa}.txt', 'rb')

        ques = list(pickle.load(file))  # Tuple converted into list.

        random.shuffle(ques)  # Question shuffled every time teh text file is opened.


    except BaseException as er3:
        messagebox.showerror("Error with database!", str(type(er3))[6:-1] + " : " + str(er3))

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


    response_signin = messagebox.askyesno("Sign In", " Would you like to Sign In?")

    if response_signin == 1:
        sign_in_GUI()

    else:
        question_fun()

# endregion



# region 2) Displaying Topics (Abhinav).



def start_fun():
    """ To display the 8 topics and choose one."""

    global img3, img4, img5, img6, img7, img8, img9, img10
    global topic_label

    starting_label.destroy()

    topic_label = LabelFrame(root_main, background="#66b3ff", height=600, width=700, bd=0)  # Reinitialized.
    topic_label.grid()         # To load/display the current working LabelFrame.

    img3 = PhotoImage(file="Resource/2) Others/Images/math.png")
    img4 = PhotoImage(file="Resource/2) Others/Images/sports.png")
    img5 = PhotoImage(file="Resource/2) Others/Images/science.png")
    img6 = PhotoImage(file="Resource/2) Others/Images/gk.png")
    img7 = PhotoImage(file="Resource/2) Others/Images/lab.png")
    img8 = PhotoImage(file="Resource/2) Others/Images/architecture.png")
    img9 = PhotoImage(file="Resource/2) Others/Images/programming.png")
    img10 = PhotoImage(file="Resource/2) Others/Images/politics.png")

    mathButton = Button(topic_label, image=img3, bg="#66b3ff", relief="raised", border=0, command= lambda : unpickle_fun("Math"))
    mathButton.place(x=175, y=100)
    math = Label(topic_label, text="Math", bg="#66b3ff", font="Cambria")
    math.place(x=175, y=170)

    sportsButton = Button(topic_label, image=img4, bg="#66b3ff", relief="raised", border=0, command= lambda : unpickle_fun("Sport"))
    sportsButton.place(x=175, y=215)
    sports = Label(topic_label, text="Sport", bg="#66b3ff", font="Cambria")
    sports.place(x=175, y=285)

    scienceButton = Button(topic_label, image=img5, bg="#66b3ff", relief="raised", border=0, command= lambda : unpickle_fun("Science"))
    scienceButton.place(x=175, y=330)
    science = Label(topic_label, text="Science", bg="#66b3ff", font="Cambria")
    science.place(x=175, y=400)


    gkButton = Button(topic_label, image=img6, bg="#66b3ff", relief="raised", border=0, command= lambda : unpickle_fun("GK"))
    gkButton.place(x=175, y=445)
    gk = Label(topic_label, text="Gk", bg="#66b3ff", font="Cambria")
    gk.place(x=175, y=515)

    labButton = Button(topic_label, image=img7, bg="#66b3ff", relief="raised", border=0, command= lambda : unpickle_fun("Lab"))
    labButton.place(x=500, y=100)
    lab = Label(topic_label, text="Lab", bg="#66b3ff", font="Cambria")
    lab.place(x=500, y=170)

    architectureButton = Button(topic_label, image=img8, bg="#66b3ff", relief="raised", command= lambda : unpickle_fun("Architecture"))
    architectureButton.place(x=500, y=215)
    architecture = Label(topic_label, text="Architecture", bg="#66b3ff", font="Cambria")
    architecture.place(x=500, y=285)

    programmingButton = Button(topic_label, image=img9, bg="#66b3ff", relief="raised", command= lambda : unpickle_fun("Programming"))
    programmingButton.place(x=500, y=330)
    programming = Label(topic_label, text="Programming", bg="#66b3ff", font="Cambria")
    programming.place(x=500, y=400)

    politicsButton = Button(topic_label, image=img10, bg="#66b3ff", relief="raised", border=0, command= lambda : unpickle_fun("Politics"))
    politicsButton.place(x=500, y=445)
    politics = Label(topic_label, text="Politics", bg="#66b3ff", font="Cambria")
    politics.place(x=500, y=515)

# endregion



# region  1) Starting (Abhinav).



root_main = Tk()
root_main.title("Quiz")
root_main.geometry("750x600")
root_main.config(background="#66b3ff")
root_main.resizable(False, False)
root_main.wm_attributes('-transparentcolor', '#AE9152')  # To make the background transparent fro Leaderboard.

question_label = LabelFrame(root_main, background="#66b3ff", height=600, width =700, bd=0)  # Question Function.

topic_label = LabelFrame(root_main, background="#66b3ff", height=600, width =700, bd=0)     # Start Function.

leaderboard_label = LabelFrame(root_main, height=600, width =750, bd=0)                     # Query Function.

frame_signin = LabelFrame(root_main, bg="white", bd=0, height=400, width=450)   # Sign In GUI Function.

frame_signup = LabelFrame(root_main, bg="white", bd=0, height=400, width=450)   # Sign Up GUI Function.


# region 1) Starting Page.

starting_label = LabelFrame(root_main, background="#66b3ff")
starting_label.pack()

img1 = PhotoImage(file="Resource/2) Others/Images/quiz.png")
labelImage = Label(starting_label, image=img1, bg="#66b3ff")
labelImage.pack(pady=(100, 0))

labelText = Label(starting_label, text="Quiz", font=("Corbel", 23, "bold"), bg="#66b3ff")
labelText.pack(pady=(5, 50))

img2 = PhotoImage(file="Resource/2) Others/Images/start-button.png")
startButton = Button(starting_label, image=img2, bg="#66b3ff", relief="flat", border=0, command=start_fun)
startButton.pack(pady=(5, 50))

labelRule = Label(starting_label,
                  text="""
                  How this Quiz works:
                  There are 8 topics to choose from.
                  Each topic has has a total of 20 questions.
                  Once you click on an option, that will be the final answer.
                  So think before you answer.
                  """,
                  width=100, font=("Cambria", 13), bg="#ff9933", fg="#000000")

labelRule.pack()



root_main.mainloop()

# endregion


# endregion



# region 0) Create Database & Table.



conn = sqlite3.connect('Resource/2) Others/Database/Player Database.db')

c = conn.cursor()

c.execute(""" CREATE TABLE IF NOT EXISTS
          information
          (
          Email text, 
          Username text,
          Password text,
          Architecture integer, 
          Lab integer,
          Math integer,
          Politics integer,
          Programming integer,
          Science integer,
          Sport integer,
          GK integer
          )""")

conn.commit()
conn.close()

# endregion



# Compiled and Managed by Sabin Maharjan.