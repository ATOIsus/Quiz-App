from tkinter import *


global choice_var
global chosen_topic
global img3, img4, img5, img6, img7, img8, img9, img10


mathQuestions = [
    "This is Math Question #1",
    "This is Math Question #2",
    "This is Math Question #3",
    "This is Math Question #4",
    "This is Math Question #5",
    "This is Math Question #6",
    "This is Math Question #7",
    "This is Math Question #8",
    "This is Math Question #9",
    "This is Math Question #10",
]
mathAnswers = [
    ["1", "2", "3", "4"],
    ["1", "2", "3", "4"],
    ["1", "2", "3", "4"],
    ["1", "2", "3", "4"],
    ["1", "2", "3", "4"],
    ["1", "2", "3", "4"],
    ["1", "2", "3", "4"],
    ["1", "2", "3", "4"],
    ["1", "2", "3", "4"],
    ["1", "2", "3", "4"],
]


def choice_selected():

    global choice_var

    print(choice_var)



def start_fun():

    starting_label.destroy()

    global chosen_topic
    global img3, img4, img5, img6, img7, img8, img9, img10


    topic_label.grid()

    chosen_topic = StringVar()

    img3 = PhotoImage(file="Resource/2) Others/Images/math.png")
    img4 = PhotoImage(file="Resource/2) Others/Images/sports.png")
    img5 = PhotoImage(file="Resource/2) Others/Images/science.png")
    img6 = PhotoImage(file="Resource/2) Others/Images/gk.png")
    img7 = PhotoImage(file="Resource/2) Others/Images/lab.png")
    img8 = PhotoImage(file="Resource/2) Others/Images/architecture.png")
    img9 = PhotoImage(file="Resource/2) Others/Images/programming.png")
    img10 = PhotoImage(file="Resource/2) Others/Images/politics.png")

    mathButton = Button(topic_label, image=img3, bg="#66b3ff", relief="raised", border=0, command=question_fun, variable = chosen_topic.set("Math"))
    mathButton.place(x=175, y=100)
    math = Label(topic_label, text="Math", bg="#66b3ff", font="Cambria")
    math.place(x=175, y=170)

    sportsButton = Button(topic_label, image=img4, bg="#66b3ff", relief="raised", border=0, command=question_fun, variable = chosen_topic.set("Sport"))
    sportsButton.place(x=175, y=215)
    sports = Label(topic_label, text="Sports", bg="#66b3ff", font="Cambria")
    sports.place(x=175, y=285)

    scienceButton = Button(topic_label, image=img5, bg="#66b3ff", relief="raised", border=0, command=question_fun, variable = chosen_topic.set("Science"))
    scienceButton.place(x=175, y=330)
    science = Label(topic_label, text="Science", bg="#66b3ff", font="Cambria")
    science.place(x=175, y=400)


    gkButton = Button(topic_label, image=img6, bg="#66b3ff", relief="raised", border=0, command=question_fun, variable = chosen_topic.set("GK"))
    gkButton.place(x=175, y=445)
    gk = Label(topic_label, text="Gk", bg="#66b3ff", font="Cambria")
    gk.place(x=175, y=515)

    labButton = Button(topic_label, image=img7, bg="#66b3ff", relief="raised", border=0, command=question_fun, variable = chosen_topic.set("Lab"))
    labButton.place(x=500, y=100)
    lab = Label(topic_label, text="Lab", bg="#66b3ff", font="Cambria")
    lab.place(x=500, y=170)

    architectureButton = Button(topic_label, image=img8, bg="#66b3ff", relief="raised", border=0, command=question_fun, variable = chosen_topic.set("Architecture"))
    architectureButton.place(x=500, y=215)
    architecture = Label(topic_label, text="Architecture", bg="#66b3ff", font="Cambria")
    architecture.place(x=500, y=285)

    programmingButton = Button(topic_label, image=img9, bg="#66b3ff", relief="raised", border=0, command=question_fun, variable = chosen_topic.set("Programming"))
    programmingButton.place(x=500, y=330)
    programming = Label(topic_label, text="Programming", bg="#66b3ff", font="Cambria")
    programming.place(x=500, y=400)

    politicsButton = Button(topic_label, image=img10, bg="#66b3ff", relief="raised", border=0, command=question_fun, variable = chosen_topic.set("Politics"))
    politicsButton.place(x=500, y=445)
    politics = Label(topic_label, text="Politics", bg="#66b3ff", font="Cambria")
    politics.place(x=500, y=515)



def question_fun():

    topic_label.destroy()

    global choice_var

    question_label.pack(pady=(100, 50), padx=(90, 100))

    labelQuestion1 = Label(question_label, text=mathQuestions[0], font=("Berlin Sans FB", 16), width=500, wraplength=400, background="#66b3ff")
    labelQuestion1.pack(pady=(100, 50), padx=(90, 100))

    choice_var = StringVar()

    r1 = Radiobutton(question_label, text=mathAnswers[0], font=("Times", 11), value=0, variable=choice_var, bg="#66b3ff", command= choice_selected)
    r1.pack()

    r2 = Radiobutton(question_label, text=mathAnswers[1], font=("Times", 11), value=1, variable=choice_var, bg="#66b3ff", command= choice_selected)
    r2.pack()

    r3 = Radiobutton(question_label, text=mathAnswers[2], font=("Times", 11), value=2, variable=choice_var,  bg="#66b3ff", command= choice_selected)
    r3.pack()

    r4 = Radiobutton(question_label, text=mathAnswers[3], font=("Times", 11), value=3, variable=choice_var,  bg="#66b3ff", command= choice_selected)
    r4.pack()




root_main = Tk()
root_main.title("Quiz")
root_main.geometry("700x600")
root_main.config(background="#66b3ff")
root_main.resizable(False, False)

question_label = LabelFrame(root_main, background="#66b3ff", height=600, width =700, bd=0)

topic_label = LabelFrame(root_main, background="#66b3ff", height=600, width =700, bd=0)



# region 1) Staring Page.

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