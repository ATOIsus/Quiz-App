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


indexes = []


def gen():
    global indexes
    while (len(indexes)) < 5:
        x = random.randint(0, 9)
        if x in indexes:
            continue
        else:
            indexes.append(x)
    print(indexes)


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


def gkClick():
    mathButton.destroy()
    sportsButton.destroy()
    scienceButton.destroy()
    gkButton.destroy()
    labButton.destroy()
    architectureButton.destroy()
    programmingButton.destroy()
    politicsButton.destroy()


def labClick():
    mathButton.destroy()
    sportsButton.destroy()
    scienceButton.destroy()
    gkButton.destroy()
    labButton.destroy()
    architectureButton.destroy()
    programmingButton.destroy()
    politicsButton.destroy()


def architectureClick():
    mathButton.destroy()
    sportsButton.destroy()
    scienceButton.destroy()
    gkButton.destroy()
    labButton.destroy()
    architectureButton.destroy()
    programmingButton.destroy()
    politicsButton.destroy()


def programmingClick():
    mathButton.destroy()
    sportsButton.destroy()
    scienceButton.destroy()
    gkButton.destroy()
    labButton.destroy()
    programmingButton.destroy()
    architectureButton.destroy()
    politicsButton.destroy()


def politicsClick():
    mathButton.destroy()
    sportsButton.destroy()
    scienceButton.destroy()
    gkButton.destroy()
    labButton.destroy()
    politicsButton.destroy()
    architectureButton.destroy()
    programmingButton.destroy()


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
mathButton.pack(pady=(90, 5), padx=(5, 400))


img4 = PhotoImage(file="sports.png")
sportsButton = Button(
    root,
    image=img4,
    bg="#66b3ff",
    relief="raised",
    border=0,
    command=sportsClick,
)
sportsButton.pack(pady=(50, 115), padx=(1, 400))


img5 = PhotoImage(file="science.png")
scienceButton = Button(
    root,
    image=img5,
    bg="#66b3ff",
    relief="raised",
    border=0,
    command=scienceClick,
)
scienceButton.pack()


img6 = PhotoImage(file="gk.png")
gkButton = Button(
    root,
    image=img6,
    bg="#66b3ff",
    relief="raised",
    border=0,
    command=gkClick,
)
gkButton.pack()


img7 = PhotoImage(file="lab.png")
labButton = Button(
    root,
    image=img7,
    bg="#66b3ff",
    relief="raised",
    border=0,
    command=labClick,
)
labButton.pack()


img8 = PhotoImage(file="architecture.png")
architectureButton = Button(
    root,
    image=img8,
    bg="#66b3ff",
    relief="raised",
    border=0,
    command=architectureClick,
)
architectureButton.pack()


img9 = PhotoImage(file="programming.png")
programmingButton = Button(
    root,
    image=img9,
    bg="#66b3ff",
    relief="raised",
    border=0,
    command=programmingClick,
)
programmingButton.pack()

img10 = PhotoImage(file="politics.png")
politicsButton = Button(
    root,
    image=img10,
    bg="#66b3ff",
    relief="raised",
    border=0,
    command=politicsClick,
)
politicsButton.pack()


root.mainloop()
