import random  # To shuffle choices.
import pickle  # To unpickle the MCQ.
import sqlite3                  # To connect to the database.
from tkinter import *           # To use basic functions and methods of tkinter.
from tkinter import messagebox  # To show popup messagebox.
from tkinter import ttk         # For the table to display the data from the database.
from PIL import Image, ImageTk  # To display images.
from playsound import playsound  # To produce sound during right, wrong answer and highest score.


# region Global Variables.

question = []  # List of all questions.
anser = []     # List of all answers.

option1 = []  # List of all option.
option2 = []  # List of all option.
option3 = []  # List of all option.

score = 0  # The number of correct answers.
ques = []  # List of all MCQs (Questions and Choices).

global ans_index         # The indexing for the answer in Supplying MCQ Function.

global choice            # For Check Function.



global img3, img4, img5, img6, img7, img8, img9, img10   # To display the images in start function.


# endregion




# region 6) Check Answer Function (Sabin).



def chk_ans(ans, k):
    """ Question and choices are displayed; the answer is checked and scored. """

    global score
    global choice

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


# region 3) Unpickle and separate MCQs (Sabin).


def unpickle_fun(quiz_topic):

    global ques

    try:
        ''' To unpickle the MCQs. '''



        file = open(f'Resource/1) Question/{quiz_topic}.txt', 'rb')

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

    supply_MCQ()

# endregion



# region 5) Displaying MCQs (Abhinav).



def question_fun(question_pa, choice1_pa, choice2_pa, choice3_pa, choice4_pa):

    topic_label.destroy()

    question_label.pack(pady=(100, 50), padx=(90, 100))

    labelQuestion1 = Label(question_label, font=("Berlin Sans FB", 16), width=500, wraplength=400, background="#66b3ff")
    labelQuestion1.pack(pady=(100, 50), padx=(90, 100))

    choice_var = IntVar()
    choice_var.set(-1)

    global ans_index

    r1 = Radiobutton(question_label, font=("Times", 11),  bg="#66b3ff", variable = choice_var, value = 0, command= lambda : chk_ans(1, ans_index))
    r1.pack()

    r2 = Radiobutton(question_label, font=("Times", 11), bg="#66b3ff", variable = choice_var, value = 0, command= lambda : chk_ans(2, ans_index))
    r2.pack()

    r3 = Radiobutton(question_label, font=("Times", 11), bg="#66b3ff", variable = choice_var, value = 0, command= lambda : chk_ans(3, ans_index))
    r3.pack()

    r4 = Radiobutton(question_label, font=("Times", 11), bg="#66b3ff", variable = choice_var, value = 0, command= lambda : chk_ans(4, ans_index))
    r4.pack()

    labelQuestion1.configure(text=question_pa)
    r1.configure(text=choice1_pa)
    r2.configure(text=choice2_pa)
    r3.configure(text=choice3_pa)
    r4.configure(text=choice4_pa)


# endregion




# region 4) Supplying MCQs (Sabin).



def supply_MCQ():

    try:

        global ans_index
        global choice

        for ans_index in range(len(ques)):

            choice = [anser[ans_index], option1[ans_index], option2[ans_index], option3[ans_index]]
            random.shuffle(choice)

            question_fun(question[ans_index], choice[0], choice[1], choice[2], choice[3])



    except BaseException as er8:
        messagebox.showerror("Error while Displaying Questions!", str(type(er8))[6:-1] + " : " + str(er8))


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

question_label = LabelFrame(root_main, background="#66b3ff", height=600, width =700, bd=0)

topic_label = LabelFrame(root_main, background="#66b3ff", height=600, width =700, bd=0)



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


