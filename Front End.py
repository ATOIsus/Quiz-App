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

ques_index = 0

global choice_var
global quiz_topic


global img3, img4, img5, img6, img7, img8, img9, img10   # To display the images in start function.
global labelQuestion1, r1, r2, r3, r4


# endregion




# region 7) Leaderboard (Sabin).



def query_fun():
    """ Shows the data of 10 users in descending order with the highest score in the selected topic. """

    global quiz_topic

    leaderboard_label.grid()

    conn = sqlite3.connect('Resource/2) Others/Database/Player Database.db')
    cur = conn.cursor()

    cur.execute(f"""SELECT ROWID, Name, Username, {quiz_topic}  FROM information 
                        ORDER BY {quiz_topic} DESC
                        LIMIT 10;""")
    rows = cur.fetchall()

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

    conn.commit()
    conn.close()

    delete_btn = Button(leaderboard_label, text="Delete")  # , command=delete_fun)
    delete_btn.grid(row=12, column=0, columnspan=2, pady=10, padx=10, ipadx=120)


# endregion




# region 6) Selected Function (Abhinav).



def selected_fun():

    global ques_index
    global labelQuestion1, r1, r2, r3, r4
    global choice
    global score


    choice_var.set(-1)


    if ques_index == 20:
        question_label.destroy()
        query_fun()


    elif ques_index < 20:
        choice = [anser[ques_index], option1[ques_index], option2[ques_index], option3[ques_index]]
        random.shuffle(choice)

        labelQuestion1.config(text=question[ques_index])
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
    """ Question and choices are displayed; the answer is checked and scored. """

    global score
    global choice
    global ques_index

    try:
        if choice[ans] == anser[k-1]:  # Check if the answer is right.
            playsound('Resource/2) Others/Sounds/correct.wav')
            score += 1

        else:
            playsound('Resource/2) Others/Sounds/incorrect.wav')


        if ques_index < 21:
            selected_fun()

        else:
            pass

    except BaseException as er5:
        messagebox.showerror("Error in Check Answer Function!", str(type(er5))[6:-1] + " : " + str(er5))


# endregion



# region 4) Displaying MCQs (Abhinav).



def question_fun():

    topic_label.destroy()

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

    if ques_index < 21:
        selected_fun()
    else:
        pass



# endregion



# region 3) Unpickle and separate MCQs (Sabin).



def unpickle_fun(quiz_topic_pa):

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

    question_fun()

# endregion



# region 2) Displaying Topics (Abhinav).



def start_fun():

    starting_label.destroy()

    global img3, img4, img5, img6, img7, img8, img9, img10


    topic_label.grid()

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

question_label = LabelFrame(root_main, background="#66b3ff", height=600, width =700, bd=0)

topic_label = LabelFrame(root_main, background="#66b3ff", height=600, width =700, bd=0)

leaderboard_label = LabelFrame(root_main, height=600, width =750, bd=0)



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



# Compiled and managed by Sabin Maharjan.