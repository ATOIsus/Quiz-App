from tkinter import *
import random

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

sportsQuestions = [
    "This is Sports Question #1",
    "This is Sports Question #2",
    "This is Sports Question #3",
    "This is Sports Question #4",
    "This is Sports Question #5",
    "This is Sports Question #6",
    "This is Sports Question #7",
    "This is Sports Question #8",
    "This is Sports Question #9",
    "This is Sports Question #10",
]
sportsAnswers = [
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

scienceQuestions = [
    "This is Science Question #1",
    "This is Science Question #2",
    "This is Science Question #3",
    "This is Science Question #4",
    "This is Science Question #5",
    "This is Science Question #6",
    "This is Science Question #7",
    "This is Science Question #8",
    "This is Science Question #9",
    "This is Science Question #10",
]
scienceAnswers = [
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

indexes = []


def gen():
    global indexes
    while (len(indexes)) < 5:
        x = random.randint(0, 9)
        if x in indexes:
            continue
        else:
            indexes.append(x)


def startButtonClick():
    labelImage.destroy()
    labelText.destroy()
    labelRule.destroy()
    startButton.destroy()


def mathClick():
    mathButton.destroy()
    sportsButton.destroy()
    scienceButton.destroy()
    gkButton.destroy()
    labButton.destroy()
    architectureButton.destroy()
    programmingButton.destroy()
    politicsButton.destroy()
    math.destroy()
    sports.destroy()
    science.destroy()
    gk.destroy()
    lab.destroy()
    architecture.destroy()
    programming.destroy()
    politics.destroy()
    gen()
    labelQuestion1 = Label(
        root,
        text=mathQuestions[indexes[0]],
        font=("Berlin Sans FB", 16),
        width=500,
        wraplength=400,
        background="#66b3ff",
    )
    labelQuestion1.pack(pady=(100, 50), padx=(90, 100))
    radiovar = IntVar()
    radiovar.set(-1)
    r1 = Radiobutton(
        root,
        text=mathAnswers[indexes[0]][0],
        font=("Times", 11),
        value=0,
        variable=radiovar,
        bg="#66b3ff"
    )
    r1.pack()

    radiovar = IntVar()
    radiovar.set(-1)
    r2 = Radiobutton(
        root,
        text=mathAnswers[indexes[0]][1],
        font=("Times", 11),
        value=1,
        variable=radiovar,
        bg="#66b3ff"
    )
    r2.pack()

    radiovar = IntVar()
    radiovar.set(-1)
    r3 = Radiobutton(
        root,
        text=mathAnswers[indexes[0]][2],
        font=("Times", 11),
        value=2,
        variable=radiovar,
        bg="#66b3ff"
    )
    r3.pack()

    radiovar = IntVar()
    radiovar.set(-1)
    r4 = Radiobutton(
        root,
        text=mathAnswers[indexes[0]][3],
        font=("Times", 11),
        value=3,
        variable=radiovar,
        bg="#66b3ff"
    )
    r4.pack()


def sportsClick():
    mathButton.destroy()
    sportsButton.destroy()
    scienceButton.destroy()
    gkButton.destroy()
    labButton.destroy()
    architectureButton.destroy()
    programmingButton.destroy()
    politicsButton.destroy()
    math.destroy()
    sports.destroy()
    science.destroy()
    gk.destroy()
    lab.destroy()
    architecture.destroy()
    programming.destroy()
    politics.destroy()
    gen()
    labelQuestion2 = Label(
        root,
        text=sportsQuestions[indexes[0]],
        font=("Berlin Sans FB", 16),
        width=500,
        justify="center",
        wraplength=400,
        background="#66b3ff",
    )
    labelQuestion2.pack(pady=(100, 50), padx=(90, 100))
    radiovar = IntVar()
    radiovar.set(-1)
    r1 = Radiobutton(
        root,
        text=sportsAnswers[indexes[0]][0],
        font=("Times", 11),
        value=0,
        variable=radiovar,
        bg="#66b3ff"
    )
    r1.pack()

    radiovar = IntVar()
    radiovar.set(-1)
    r2 = Radiobutton(
        root,
        text=sportsAnswers[indexes[0]][1],
        font=("Times", 11),
        value=1,
        variable=radiovar,
        bg="#66b3ff"
    )
    r2.pack()

    radiovar = IntVar()
    radiovar.set(-1)
    r3 = Radiobutton(
        root,
        text=sportsAnswers[indexes[0]][2],
        font=("Times", 11),
        value=2,
        variable=radiovar,
        bg="#66b3ff"
    )
    r3.pack()

    radiovar = IntVar()
    radiovar.set(-1)
    r4 = Radiobutton(
        root,
        text=sportsAnswers[indexes[0]][3],
        font=("Times", 11),
        value=3,
        variable=radiovar,
        bg="#66b3ff"
    )
    r4.pack()


def scienceClick():
    mathButton.destroy()
    sportsButton.destroy()
    scienceButton.destroy()
    gkButton.destroy()
    labButton.destroy()
    architectureButton.destroy()
    programmingButton.destroy()
    politicsButton.destroy()
    math.destroy()
    sports.destroy()
    science.destroy()
    gk.destroy()
    lab.destroy()
    architecture.destroy()
    programming.destroy()
    politics.destroy()
    gen()
    labelQuestion3 = Label(
        root,
        text=scienceQuestions[indexes[0]],
        font=("Berlin Sans FB", 16),
        width=500,
        justify="center",
        wraplength=400,
        background="#66b3ff",
    )
    labelQuestion3.pack(pady=(100, 50), padx=(90, 100))
    radiovar = IntVar()
    radiovar.set(-1)
    r1 = Radiobutton(
        root,
        text=scienceAnswers[indexes[0]][0],
        font=("Times", 11),
        value=0,
        variable=radiovar,
        bg="#66b3ff"
    )
    r1.pack()

    radiovar = IntVar()
    radiovar.set(-1)
    r2 = Radiobutton(
        root,
        text=scienceAnswers[indexes[0]][1],
        font=("Times", 11),
        value=1,
        variable=radiovar,
        bg="#66b3ff"
    )
    r2.pack()

    radiovar = IntVar()
    radiovar.set(-1)
    r3 = Radiobutton(
        root,
        text=scienceAnswers[indexes[0]][2],
        font=("Times", 11),
        value=2,
        variable=radiovar,
        bg="#66b3ff"
    )
    r3.pack()

    radiovar = IntVar()
    radiovar.set(-1)
    r4 = Radiobutton(
        root,
        text=scienceAnswers[indexes[0]][3],
        font=("Times", 11),
        value=3,
        variable=radiovar,
        bg="#66b3ff"
    )
    r4.pack()


def gkClick():
    mathButton.destroy()
    sportsButton.destroy()
    scienceButton.destroy()
    gkButton.destroy()
    labButton.destroy()
    architectureButton.destroy()
    programmingButton.destroy()
    politicsButton.destroy()
    math.destroy()
    sports.destroy()
    science.destroy()
    gk.destroy()
    lab.destroy()
    architecture.destroy()
    programming.destroy()
    politics.destroy()


def labClick():
    mathButton.destroy()
    sportsButton.destroy()
    scienceButton.destroy()
    gkButton.destroy()
    labButton.destroy()
    architectureButton.destroy()
    programmingButton.destroy()
    politicsButton.destroy()
    math.destroy()
    sports.destroy()
    science.destroy()
    gk.destroy()
    lab.destroy()
    architecture.destroy()
    programming.destroy()
    politics.destroy()


def architectureClick():
    mathButton.destroy()
    sportsButton.destroy()
    scienceButton.destroy()
    gkButton.destroy()
    labButton.destroy()
    architectureButton.destroy()
    programmingButton.destroy()
    politicsButton.destroy()
    math.destroy()
    sports.destroy()
    science.destroy()
    gk.destroy()
    lab.destroy()
    architecture.destroy()
    programming.destroy()
    politics.destroy()


def programmingClick():
    mathButton.destroy()
    sportsButton.destroy()
    scienceButton.destroy()
    gkButton.destroy()
    labButton.destroy()
    programmingButton.destroy()
    architectureButton.destroy()
    politicsButton.destroy()
    math.destroy()
    sports.destroy()
    science.destroy()
    gk.destroy()
    lab.destroy()
    architecture.destroy()
    programming.destroy()
    politics.destroy()


def politicsClick():
    mathButton.destroy()
    sportsButton.destroy()
    scienceButton.destroy()
    gkButton.destroy()
    labButton.destroy()
    politicsButton.destroy()
    architectureButton.destroy()
    programmingButton.destroy()
    math.destroy()
    sports.destroy()
    science.destroy()
    gk.destroy()
    lab.destroy()
    architecture.destroy()
    programming.destroy()
    politics.destroy()


root = Tk()
root.title("Quiz")
root.geometry("700x600")
root.config(background="#66b3ff")
root.resizable(False, False)


img1 = PhotoImage(file="quiz.png")
labelImage = Label(
    root,
    image=img1,
    bg="#66b3ff",
)
labelImage.pack(pady=(100, 0))

labelText = Label(
    root,
    text="Quiz",
    font=("Corbel", 23, "bold"),
    bg="#66b3ff",
)
labelText.pack(pady=(5, 50))

img2 = PhotoImage(file="start-button.png")
startButton = Button(
    root,
    image=img2,
    bg="#66b3ff",
    relief="flat",
    border=0,
    command=startButtonClick,
)
startButton.pack(pady=(5, 50))

labelRule = Label(
    root,
    text="""
    How this Quiz works?
    This Quiz has a total of ___ questions
    You will have 30 seconds to answer each questions
    Once you click on an option, that will be the final answer
    So think before you answer
    """,
    width=100,
    font=("Cambria", 13),
    bg="#ff9933",
    fg="#000000",
)
labelRule.pack()

img3 = PhotoImage(file="math.png")
mathButton = Button(
    root,
    image=img3,
    bg="#66b3ff",
    relief="raised",
    border=0,
    command=mathClick,
)
mathButton.place(x=175, y=100)
math = Label(
    root,
    text="Math",
    bg="#66b3ff",
    font="Cambria",
)
math.place(x=175, y=170)

img4 = PhotoImage(file="sports.png")
sportsButton = Button(
    root,
    image=img4,
    bg="#66b3ff",
    relief="raised",
    border=0,
    command=sportsClick,
)
sportsButton.place(x=175, y=215)
sports = Label(
    root,
    text="Sports",
    bg="#66b3ff",
    font="Cambria",
)
sports.place(x=175, y=285)

img5 = PhotoImage(file="science.png")
scienceButton = Button(
    root,
    image=img5,
    bg="#66b3ff",
    relief="raised",
    border=0,
    command=scienceClick,
)
scienceButton.place(x=175, y=330)
science = Label(
    root,
    text="Science",
    bg="#66b3ff",
    font="Cambria",
)
science.place(x=175, y=400)

img6 = PhotoImage(file="gk.png")
gkButton = Button(
    root,
    image=img6,
    bg="#66b3ff",
    relief="raised",
    border=0,
    command=gkClick,
)
gkButton.place(x=175, y=445)
gk = Label(
    root,
    text="Gk",
    bg="#66b3ff",
    font="Cambria",
)
gk.place(x=175, y=515)

img7 = PhotoImage(file="lab.png")
labButton = Button(
    root,
    image=img7,
    bg="#66b3ff",
    relief="raised",
    border=0,
    command=labClick,
)
labButton.place(x=500, y=100)
lab = Label(
    root,
    text="Lab",
    bg="#66b3ff",
    font="Cambria",
)
lab.place(x=500, y=170)

img8 = PhotoImage(file="architecture.png")
architectureButton = Button(
    root,
    image=img8,
    bg="#66b3ff",
    relief="raised",
    border=0,
    command=architectureClick,
)
architectureButton.place(x=500, y=215)
architecture = Label(
    root,
    text="Architecture",
    bg="#66b3ff",
    font="Cambria",
)
architecture.place(x=500, y=285)

img9 = PhotoImage(file="programming.png")
programmingButton = Button(
    root,
    image=img9,
    bg="#66b3ff",
    relief="raised",
    border=0,
    command=programmingClick,
)
programmingButton.place(x=500, y=330)
programming = Label(
    root,
    text="Programming",
    bg="#66b3ff",
    font="Cambria",
)
programming.place(x=500, y=400)

img10 = PhotoImage(file="politics.png")
politicsButton = Button(
    root,
    image=img10,
    bg="#66b3ff",
    relief="raised",
    border=0,
    command=politicsClick,
)
politicsButton.place(x=500, y=445)
politics = Label(
    root,
    text="Politics",
    bg="#66b3ff",
    font="Cambria",
)
politics.place(x=500, y=515)

root.mainloop()
