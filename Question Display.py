from tkinter import *

global radioVar

indexes = []

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


def mathSelected():
    """
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
    """

    global radioVar

    root2 = Tk()
    root2.title("Quiz")
    root2.geometry("700x600")
    root2.config(background="#66b3ff")
    root2.resizable(False, False)

    labelQuestion1 = Label(root2, text=mathQuestions[0], font=("Berlin Sans FB", 16), width=500, wraplength=400, background="#66b3ff")
    labelQuestion1.pack(pady=(100, 50), padx=(90, 100))

    radioVar = IntVar()
    radioVar.set(-1)

    r1 = Radiobutton(root2, text=mathAnswers[0], font=("Times", 11), value=0, variable=radioVar, bg="#66b3ff")  # ,command=mathSelected)
    r1.pack()

    r2 = Radiobutton(root2, text=mathAnswers[1], font=("Times", 11), value=1, variable=radioVar, bg="#66b3ff")  # ,command=mathSelected)
    r2.pack()

    r3 = Radiobutton(root2, text=mathAnswers[2], font=("Times", 11), value=2, variable=radioVar,  bg="#66b3ff")  # ,command=mathSelected)
    r3.pack()

    r4 = Radiobutton(root2, text=mathAnswers[3], font=("Times", 11), value=3, variable=radioVar,  bg="#66b3ff")  # ,command=mathSelected)
    r4.pack()

    root2.mainloop()


mathSelected()