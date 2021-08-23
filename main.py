from tkinter import *


def startButtonClick():
    labelImage.destroy()
    labelText.destroy()
    labelRule.destroy()
    startButton.destroy()


root = Tk()
root.title("Quiz")
root.geometry("700x600")
root.config(background="#66b3ff")
root.resizable(False, False)


img1 = PhotoImage(file="quiz.png")
labelImage = Label(
    root,
    image=img1,
    background="#66b3ff",
)
labelImage.pack(pady=(100, 0))


labelText = Label(
    root,
    text="Quiz",
    font=("Corbel", 23, "bold"),
    background="#66b3ff",
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
    background="#ff9933",
    foreground="#000000",
)
labelRule.pack()


root.mainloop()
