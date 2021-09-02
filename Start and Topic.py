from tkinter import *



def Click():

    root.destroy()

    root2 = Tk()
    root2.title("Quiz")
    root2.geometry("700x600")
    root2.config(background="#66b3ff")
    root2.resizable(False, False)

    img3 = PhotoImage(file="Resource/2) Others/Images/math.png")
    mathButton = Button(root2, image=img3, bg="#66b3ff", relief="raised", border=0)   # command=Click() )
    mathButton.place(x=175, y=100)
    math = Label(root2, text="Math", bg="#66b3ff", font="Cambria")
    math.place(x=175, y=170)

    img4 = PhotoImage(file="Resource/2) Others/Images/sports.png")
    sportsButton = Button(root2, image=img4, bg="#66b3ff", relief="raised", border=0)  # command=Click() )
    sportsButton.place(x=175, y=215)
    sports = Label(root2, text="Sports", bg="#66b3ff", font="Cambria")
    sports.place(x=175, y=285)

    img5 = PhotoImage(file="Resource/2) Others/Images/science.png")
    scienceButton = Button(root2, image=img5, bg="#66b3ff", relief="raised", border=0,)  # command=Click() )
    scienceButton.place(x=175, y=330)
    science = Label(root2, text="Science", bg="#66b3ff", font="Cambria")
    science.place(x=175, y=400)


    img6 = PhotoImage(file="Resource/2) Others/Images/gk.png")
    gkButton = Button(root2, image=img6, bg="#66b3ff", relief="raised", border=0)   # command=Click, )
    gkButton.place(x=175, y=445)
    gk = Label(root2, text="Gk", bg="#66b3ff", font="Cambria")
    gk.place(x=175, y=515)

    img7 = PhotoImage(file="Resource/2) Others/Images/lab.png")
    labButton = Button(root2, image=img7, bg="#66b3ff", relief="raised", border=0)  # command=Click )
    labButton.place(x=500, y=100)
    lab = Label(root2, text="Lab", bg="#66b3ff", font="Cambria")
    lab.place(x=500, y=170)

    img8 = PhotoImage(file="Resource/2) Others/Images/architecture.png")
    architectureButton = Button(root2, image=img8, bg="#66b3ff", relief="raised", border=0)  # command=Click)
    architectureButton.place(x=500, y=215)
    architecture = Label(root2, text="Architecture", bg="#66b3ff", font="Cambria")
    architecture.place(x=500, y=285)

    img9 = PhotoImage(file="Resource/2) Others/Images/programming.png")
    programmingButton = Button(root2, image=img9, bg="#66b3ff", relief="raised", border=0)  # command=Click)
    programmingButton.place(x=500, y=330)
    programming = Label(root2, text="Programming", bg="#66b3ff", font="Cambria")
    programming.place(x=500, y=400)

    img10 = PhotoImage(file="Resource/2) Others/Images/politics.png")
    politicsButton = Button(root2, image=img10, bg="#66b3ff", relief="raised", border=0)  # command=Click,)
    politicsButton.place(x=500, y=445)
    politics = Label(root2, text="Politics", bg="#66b3ff", font="Cambria")
    politics.place(x=500, y=515)

    root2.mainloop()




# region 1) Staring Page.



root = Tk()
root.title("Quiz")
root.geometry("700x600")
root.config(background="#66b3ff")
root.resizable(False, False)

img1 = PhotoImage(file="Resource/2) Others/Images/quiz.png")
labelImage = Label(root, image=img1, bg="#66b3ff")
labelImage.pack(pady=(100, 0))

labelText = Label(root, text="Quiz", font=("Corbel", 23, "bold"), bg="#66b3ff")
labelText.pack(pady=(5, 50))

img2 = PhotoImage(file="Resource/2) Others/Images/start-button.png")
startButton = Button(root, image=img2, bg="#66b3ff", relief="flat", border=0, command=Click)
startButton.pack(pady=(5, 50))

labelRule = Label(root,
                  text="""
                  How this Quiz works:
                  There are 8 topics to choose from.
                  Each topic has has a total of 20 questions.
                  Once you click on an option, that will be the final answer.
                  So think before you answer.
                  """,
                  width=100, font=("Cambria", 13), bg="#ff9933", fg="#000000")

labelRule.pack()

root.mainloop()

# endregion