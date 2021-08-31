from tkinter import *
import random


def startButtonClick():
    labelImage.destroy()
    labelText.destroy()
    labelRule.destroy()
    startButton.destroy()
    root.destroy()
    newWindow1()


user_answer = []
indexes = []
ques = 1


def newWindow1():
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

    gkQuestions = [
        "This is Gk Question #1",
        "This is Gk Question #2",
        "This is Gk Question #3",
        "This is Gk Question #4",
        "This is Gk Question #5",
        "This is Gk Question #6",
        "This is Gk Question #7",
        "This is Gk Question #8",
        "This is Gk Question #9",
        "This is Gk Question #10",
    ]
    gkAnswers = [
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

    labQuestions = [
        "This is Lab Question #1",
        "This is Lab Question #2",
        "This is Lab Question #3",
        "This is Lab Question #4",
        "This is Lab Question #5",
        "This is Lab Question #6",
        "This is Lab Question #7",
        "This is Lab Question #8",
        "This is Lab Question #9",
        "This is Lab Question #10",
    ]
    labAnswers = [
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

    architectureQuestions = [
        "This is Architecture Question #1",
        "This is Architecture Question #2",
        "This is Architecture Question #3",
        "This is Architecture Question #4",
        "This is Architecture Question #5",
        "This is Architecture Question #6",
        "This is Architecture Question #7",
        "This is Architecture Question #8",
        "This is Architecture Question #9",
        "This is Architecture Question #10",
    ]
    architectureAnswers = [
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

    programmingQuestions = [
        "This is Programming Question #1",
        "This is Programming Question #2",
        "This is Programming Question #3",
        "This is Programming Question #4",
        "This is Programming Question #5",
        "This is Programming Question #6",
        "This is Programming Question #7",
        "This is Programming Question #8",
        "This is Programming Question #9",
        "This is Programming Question #10",
    ]
    programmingAnswers = [
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

    politicsQuestions = [
        "This is Politics Question #1",
        "This is Politics Question #2",
        "This is Politics Question #3",
        "This is Politics Question #4",
        "This is Politics Question #5",
        "This is Politics Question #6",
        "This is Politics Question #7",
        "This is Politics Question #8",
        "This is Politics Question #9",
        "This is Politics Question #10",
    ]
    politicsAnswers = [
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

    def gen():
        global indexes
        while (len(indexes)) < 10:
            x = random.randint(0, 9)
            if x in indexes:
                continue
            else:
                indexes.append(x)

    def mathSelected():
        global radioVar, user_answer
        global labelQuestion1, r1, r2, r3, r4
        global ques
        x = radioVar.get()
        user_answer.append(x)
        radioVar.set(-1)
        if ques < 10:
            labelQuestion1.config(text=mathQuestions[indexes[ques]])
            r1['text'] = mathAnswers[indexes[ques]][0]
            r2['text'] = mathAnswers[indexes[ques]][1]
            r3['text'] = mathAnswers[indexes[ques]][2]
            r4['text'] = mathAnswers[indexes[ques]][3]
            ques += 1
        else:
            # print(indexes)
            # print(user_answer)
            # these two lines were just developement code
            # we don't need them
            pass

    def sportsSelected():
        global radioVar, user_answer
        global labelQuestion2, r1, r2, r3, r4
        global ques
        x = radioVar.get()
        user_answer.append(x)
        radioVar.set(-1)
        if ques < 10:
            labelQuestion2.config(text=sportsQuestions[indexes[ques]])
            r1['text'] = sportsAnswers[indexes[ques]][0]
            r2['text'] = sportsAnswers[indexes[ques]][1]
            r3['text'] = sportsAnswers[indexes[ques]][2]
            r4['text'] = sportsAnswers[indexes[ques]][3]
            ques += 1
        else:
            # print(indexes)
            # print(user_answer)
            # these two lines were just developement code
            # we don't need them
            pass

    def scienceSelected():
        global radioVar, user_answer
        global labelQuestion3, r1, r2, r3, r4
        global ques
        x = radioVar.get()
        user_answer.append(x)
        radioVar.set(-1)
        if ques < 10:
            labelQuestion3.config(text=scienceQuestions[indexes[ques]])
            r1['text'] = scienceAnswers[indexes[ques]][0]
            r2['text'] = scienceAnswers[indexes[ques]][1]
            r3['text'] = scienceAnswers[indexes[ques]][2]
            r4['text'] = scienceAnswers[indexes[ques]][3]
            ques += 1
        else:
            # print(indexes)
            # print(user_answer)
            # these two lines were just developement code
            # we don't need them
            pass

    def gkSelected():
        global radioVar, user_answer
        global labelQuestion4, r1, r2, r3, r4
        global ques
        x = radioVar.get()
        user_answer.append(x)
        radioVar.set(-1)
        if ques < 10:
            labelQuestion4.config(text=gkQuestions[indexes[ques]])
            r1['text'] = gkAnswers[indexes[ques]][0]
            r2['text'] = gkAnswers[indexes[ques]][1]
            r3['text'] = gkAnswers[indexes[ques]][2]
            r4['text'] = gkAnswers[indexes[ques]][3]
            ques += 1
        else:
            # print(indexes)
            # print(user_answer)
            # these two lines were just developement code
            # we don't need them
            pass

    def labSelected():
        global radioVar, user_answer
        global labelQuestion5, r1, r2, r3, r4
        global ques
        x = radioVar.get()
        user_answer.append(x)
        radioVar.set(-1)
        if ques < 10:
            labelQuestion5.config(text=labQuestions[indexes[ques]])
            r1['text'] = labAnswers[indexes[ques]][0]
            r2['text'] = labAnswers[indexes[ques]][1]
            r3['text'] = labAnswers[indexes[ques]][2]
            r4['text'] = labAnswers[indexes[ques]][3]
            ques += 1
        else:
            # print(indexes)
            # print(user_answer)
            # these two lines were just developement code
            # we don't need them
            pass

    def architectureSelected():
        global radioVar, user_answer
        global labelQuestion6, r1, r2, r3, r4
        global ques
        x = radioVar.get()
        user_answer.append(x)
        radioVar.set(-1)
        if ques < 10:
            labelQuestion6.config(text=architectureQuestions[indexes[ques]])
            r1['text'] = architectureAnswers[indexes[ques]][0]
            r2['text'] = architectureAnswers[indexes[ques]][1]
            r3['text'] = architectureAnswers[indexes[ques]][2]
            r4['text'] = architectureAnswers[indexes[ques]][3]
            ques += 1
        else:
            # print(indexes)
            # print(user_answer)
            # these two lines were just developement code
            # we don't need them
            pass

    def programmingSelected():
        global radioVar, user_answer
        global labelQuestion7, r1, r2, r3, r4
        global ques
        x = radioVar.get()
        user_answer.append(x)
        radioVar.set(-1)
        if ques < 10:
            labelQuestion7.config(text=programmingQuestions[indexes[ques]])
            r1['text'] = programmingAnswers[indexes[ques]][0]
            r2['text'] = programmingAnswers[indexes[ques]][1]
            r3['text'] = programmingAnswers[indexes[ques]][2]
            r4['text'] = programmingAnswers[indexes[ques]][3]
            ques += 1
        else:
            # print(indexes)
            # print(user_answer)
            # these two lines were just developement code
            # we don't need them
            pass

    def politicsSelected():
        global radioVar, user_answer
        global labelQuestion8, r1, r2, r3, r4
        global ques
        x = radioVar.get()
        user_answer.append(x)
        radioVar.set(-1)
        if ques < 10:
            labelQuestion8.config(text=politicsQuestions[indexes[ques]])
            r1['text'] = politicsAnswers[indexes[ques]][0]
            r2['text'] = politicsAnswers[indexes[ques]][1]
            r3['text'] = politicsAnswers[indexes[ques]][2]
            r4['text'] = politicsAnswers[indexes[ques]][3]
            ques += 1
        else:
            # print(indexes)
            # print(user_answer)
            # these two lines were just developement code
            # we don't need them
            pass

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
        global labelQuestion1, r1, r2, r3, r4
        labelQuestion1 = Label(
            root2,
            text=mathQuestions[indexes[0]],
            font=("Berlin Sans FB", 16),
            width=500,
            wraplength=400,
            background="#66b3ff",
        )
        labelQuestion1.pack(pady=(100, 50), padx=(90, 100))

        global radioVar
        radioVar = IntVar()
        radioVar.set(-1)

        r1 = Radiobutton(
            root2,
            text=mathAnswers[indexes[0]][0],
            font=("Times", 11),
            value=0,
            variable=radioVar,
            command=mathSelected,
            bg="#66b3ff"
        )
        r1.pack()

        r2 = Radiobutton(
            root2,
            text=mathAnswers[indexes[0]][1],
            font=("Times", 11),
            value=1,
            variable=radioVar,
            command=mathSelected,
            bg="#66b3ff"
        )
        r2.pack()

        r3 = Radiobutton(
            root2,
            text=mathAnswers[indexes[0]][2],
            font=("Times", 11),
            value=2,
            variable=radioVar,
            command=mathSelected,
            bg="#66b3ff"
        )
        r3.pack()

        r4 = Radiobutton(
            root2,
            text=mathAnswers[indexes[0]][3],
            font=("Times", 11),
            value=3,
            variable=radioVar,
            command=mathSelected,
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
        global labelQuestion2, r1, r2, r3, r4
        labelQuestion2 = Label(
            root2,
            text=sportsQuestions[indexes[0]],
            font=("Berlin Sans FB", 16),
            width=500,
            justify="center",
            wraplength=400,
            background="#66b3ff",
        )
        labelQuestion2.pack(pady=(100, 50), padx=(90, 100))

        global radioVar
        radioVar = IntVar()
        radioVar.set(-1)

        r1 = Radiobutton(
            root2,
            text=sportsAnswers[indexes[0]][0],
            font=("Times", 11),
            value=0,
            variable=radioVar,
            command=sportsSelected,
            bg="#66b3ff"
        )
        r1.pack()

        r2 = Radiobutton(
            root2,
            text=sportsAnswers[indexes[0]][1],
            font=("Times", 11),
            value=1,
            variable=radioVar,
            command=sportsSelected,
            bg="#66b3ff"
        )
        r2.pack()

        r3 = Radiobutton(
            root2,
            text=sportsAnswers[indexes[0]][2],
            font=("Times", 11),
            value=2,
            variable=radioVar,
            command=sportsSelected,
            bg="#66b3ff"
        )
        r3.pack()

        r4 = Radiobutton(
            root2,
            text=sportsAnswers[indexes[0]][3],
            font=("Times", 11),
            value=3,
            variable=radioVar,
            command=sportsSelected,
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
        global labelQuestion3, r1, r2, r3, r4
        labelQuestion3 = Label(
            root2,
            text=scienceQuestions[indexes[0]],
            font=("Berlin Sans FB", 16),
            width=500,
            justify="center",
            wraplength=400,
            background="#66b3ff",
        )
        labelQuestion3.pack(pady=(100, 50), padx=(90, 100))

        global radioVar
        radioVar = IntVar()
        radioVar.set(-1)

        r1 = Radiobutton(
            root2,
            text=scienceAnswers[indexes[0]][0],
            font=("Times", 11),
            value=0,
            variable=radioVar,
            command=scienceSelected,
            bg="#66b3ff"
        )
        r1.pack()

        r2 = Radiobutton(
            root2,
            text=scienceAnswers[indexes[0]][1],
            font=("Times", 11),
            value=1,
            variable=radioVar,
            command=scienceSelected,
            bg="#66b3ff"
        )
        r2.pack()

        r3 = Radiobutton(
            root2,
            text=scienceAnswers[indexes[0]][2],
            font=("Times", 11),
            value=2,
            variable=radioVar,
            command=scienceSelected,
            bg="#66b3ff"
        )
        r3.pack()

        r4 = Radiobutton(
            root2,
            text=scienceAnswers[indexes[0]][3],
            font=("Times", 11),
            value=3,
            variable=radioVar,
            command=scienceSelected,
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
        gen()
        global labelQuestion4, r1, r2, r3, r4
        labelQuestion4 = Label(
            root2,
            text=gkQuestions[indexes[0]],
            font=("Berlin Sans FB", 16),
            width=500,
            justify="center",
            wraplength=400,
            background="#66b3ff",
        )
        labelQuestion4.pack(pady=(100, 50), padx=(90, 100))

        global radioVar
        radioVar = IntVar()
        radioVar.set(-1)

        r1 = Radiobutton(
            root2,
            text=gkAnswers[indexes[0]][0],
            font=("Times", 11),
            value=0,
            variable=radioVar,
            command=gkSelected,
            bg="#66b3ff"
        )
        r1.pack()

        r2 = Radiobutton(
            root2,
            text=gkAnswers[indexes[0]][1],
            font=("Times", 11),
            value=1,
            variable=radioVar,
            command=gkSelected,
            bg="#66b3ff"
        )
        r2.pack()

        r3 = Radiobutton(
            root2,
            text=gkAnswers[indexes[0]][2],
            font=("Times", 11),
            value=2,
            variable=radioVar,
            command=gkSelected,
            bg="#66b3ff"
        )
        r3.pack()

        r4 = Radiobutton(
            root2,
            text=gkAnswers[indexes[0]][3],
            font=("Times", 11),
            value=3,
            variable=radioVar,
            command=gkSelected,
            bg="#66b3ff"
        )
        r4.pack()

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
        gen()

        global labelQuestion5, r1, r2, r3, r4
        labelQuestion5 = Label(
            root2,
            text=labQuestions[indexes[0]],
            font=("Berlin Sans FB", 16),
            width=500,
            justify="center",
            wraplength=400,
            background="#66b3ff",
        )
        labelQuestion5.pack(pady=(100, 50), padx=(90, 100))

        global radioVar
        radioVar = IntVar()
        radioVar.set(-1)

        r1 = Radiobutton(
            root2,
            text=labAnswers[indexes[0]][0],
            font=("Times", 11),
            value=0,
            variable=radioVar,
            command=labSelected,
            bg="#66b3ff"
        )
        r1.pack()

        r2 = Radiobutton(
            root2,
            text=labAnswers[indexes[0]][1],
            font=("Times", 11),
            value=1,
            variable=radioVar,
            command=labSelected,
            bg="#66b3ff"
        )
        r2.pack()

        r3 = Radiobutton(
            root2,
            text=labAnswers[indexes[0]][2],
            font=("Times", 11),
            value=2,
            variable=radioVar,
            command=labSelected,
            bg="#66b3ff"
        )
        r3.pack()

        r4 = Radiobutton(
            root2,
            text=labAnswers[indexes[0]][3],
            font=("Times", 11),
            value=3,
            variable=radioVar,
            command=labSelected,
            bg="#66b3ff"
        )
        r4.pack()

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
        gen()
        global labelQuestion6, r1, r2, r3, r4
        labelQuestion6 = Label(
            root2,
            text=architectureQuestions[indexes[0]],
            font=("Berlin Sans FB", 16),
            width=500,
            justify="center",
            wraplength=400,
            background="#66b3ff",
        )
        labelQuestion6.pack(pady=(100, 50), padx=(90, 100))

        global radioVar
        radioVar = IntVar()
        radioVar.set(-1)

        r1 = Radiobutton(
            root2,
            text=architectureAnswers[indexes[0]][0],
            font=("Times", 11),
            value=0,
            variable=radioVar,
            command=architectureSelected,
            bg="#66b3ff"
        )
        r1.pack()

        r2 = Radiobutton(
            root2,
            text=architectureAnswers[indexes[0]][1],
            font=("Times", 11),
            value=1,
            variable=radioVar,
            command=architectureSelected,
            bg="#66b3ff"
        )
        r2.pack()

        r3 = Radiobutton(
            root2,
            text=architectureAnswers[indexes[0]][2],
            font=("Times", 11),
            value=2,
            variable=radioVar,
            command=architectureSelected,
            bg="#66b3ff"
        )
        r3.pack()

        r4 = Radiobutton(
            root2,
            text=architectureAnswers[indexes[0]][3],
            font=("Times", 11),
            value=3,
            variable=radioVar,
            command=architectureSelected,
            bg="#66b3ff"
        )
        r4.pack()

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
        gen()
        global labelQuestion7, r1, r2, r3, r4
        labelQuestion7 = Label(
            root2,
            text=programmingQuestions[indexes[0]],
            font=("Berlin Sans FB", 16),
            width=500,
            justify="center",
            wraplength=400,
            background="#66b3ff",
        )
        labelQuestion7.pack(pady=(100, 50), padx=(90, 100))

        global radioVar
        radioVar = IntVar()
        radioVar.set(-1)

        r1 = Radiobutton(
            root2,
            text=programmingAnswers[indexes[0]][0],
            font=("Times", 11),
            value=0,
            variable=radioVar,
            command=programmingSelected,
            bg="#66b3ff"
        )
        r1.pack()

        r2 = Radiobutton(
            root2,
            text=programmingAnswers[indexes[0]][1],
            font=("Times", 11),
            value=1,
            variable=radioVar,
            command=programmingSelected,
            bg="#66b3ff"
        )
        r2.pack()

        r3 = Radiobutton(
            root2,
            text=programmingAnswers[indexes[0]][2],
            font=("Times", 11),
            value=2,
            variable=radioVar,
            command=programmingSelected,
            bg="#66b3ff"
        )
        r3.pack()

        r4 = Radiobutton(
            root2,
            text=programmingAnswers[indexes[0]][3],
            font=("Times", 11),
            value=3,
            variable=radioVar,
            command=programmingSelected,
            bg="#66b3ff"
        )
        r4.pack()

    def politicsClick():
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
        gen()
        global labelQuestion8, r1, r2, r3, r4
        labelQuestion8 = Label(
            root2,
            text=politicsQuestions[indexes[0]],
            font=("Berlin Sans FB", 16),
            width=500,
            justify="center",
            wraplength=400,
            background="#66b3ff",
        )
        labelQuestion8.pack(pady=(100, 50), padx=(90, 100))

        global radioVar
        radioVar = IntVar()
        radioVar.set(-1)

        r1 = Radiobutton(
            root2,
            text=politicsAnswers[indexes[0]][0],
            font=("Times", 11),
            value=0,
            variable=radioVar,
            command=politicsSelected,
            bg="#66b3ff"
        )
        r1.pack()

        r2 = Radiobutton(
            root2,
            text=politicsAnswers[indexes[0]][1],
            font=("Times", 11),
            value=1,
            variable=radioVar,
            command=politicsSelected,
            bg="#66b3ff"
        )
        r2.pack()

        r3 = Radiobutton(
            root2,
            text=politicsAnswers[indexes[0]][2],
            font=("Times", 11),
            value=2,
            variable=radioVar,
            command=politicsSelected,
            bg="#66b3ff"
        )
        r3.pack()

        r4 = Radiobutton(
            root2,
            text=politicsAnswers[indexes[0]][3],
            font=("Times", 11),
            value=3,
            variable=radioVar,
            command=politicsSelected,
            bg="#66b3ff"
        )
        r4.pack()

    root2 = Tk()
    root2.title("Quiz")
    root2.geometry("700x600")
    root2.config(background="#66b3ff")
    root2.resizable(False, False)

    img3 = PhotoImage(file="math.png")
    mathButton = Button(
        root2,
        image=img3,
        bg="#66b3ff",
        relief="raised",
        border=0,
        command=mathClick,
    )
    mathButton.place(x=175, y=100)
    math = Label(
        root2,
        text="Math",
        bg="#66b3ff",
        font="Cambria",
    )
    math.place(x=175, y=170)

    img4 = PhotoImage(file="sports.png")
    sportsButton = Button(
        root2,
        image=img4,
        bg="#66b3ff",
        relief="raised",
        command=sportsClick,
        border=0,
    )
    sportsButton.place(x=175, y=215)
    sports = Label(
        root2,
        text="Sports",
        bg="#66b3ff",
        font="Cambria",
    )
    sports.place(x=175, y=285)

    img5 = PhotoImage(file="science.png")
    scienceButton = Button(
        root2,
        image=img5,
        bg="#66b3ff",
        relief="raised",
        command=scienceClick,
        border=0,
    )
    scienceButton.place(x=175, y=330)
    science = Label(
        root2,
        text="Science",
        bg="#66b3ff",
        font="Cambria",
    )
    science.place(x=175, y=400)
    img6 = PhotoImage(file="gk.png")
    gkButton = Button(
        root2,
        image=img6,
        bg="#66b3ff",
        relief="raised",
        command=gkClick,
        border=0,
    )
    gkButton.place(x=175, y=445)
    gk = Label(
        root2,
        text="Gk",
        bg="#66b3ff",
        font="Cambria",
    )
    gk.place(x=175, y=515)

    img7 = PhotoImage(file="lab.png")
    labButton = Button(
        root2,
        image=img7,
        bg="#66b3ff",
        relief="raised",
        command=labClick,
        border=0,
    )
    labButton.place(x=500, y=100)
    lab = Label(
        root2,
        text="Lab",
        bg="#66b3ff",
        font="Cambria",
    )
    lab.place(x=500, y=170)

    img8 = PhotoImage(file="architecture.png")
    architectureButton = Button(
        root2,
        image=img8,
        bg="#66b3ff",
        relief="raised",
        command=architectureClick,
        border=0,
    )
    architectureButton.place(x=500, y=215)
    architecture = Label(
        root2,
        text="Architecture",
        bg="#66b3ff",
        font="Cambria",
    )
    architecture.place(x=500, y=285)

    img9 = PhotoImage(file="programming.png")
    programmingButton = Button(
        root2,
        image=img9,
        bg="#66b3ff",
        relief="raised",
        command=programmingClick,
        border=0,
    )
    programmingButton.place(x=500, y=330)
    programming = Label(
        root2,
        text="Programming",
        bg="#66b3ff",
        font="Cambria",
    )
    programming.place(x=500, y=400)

    img10 = PhotoImage(file="politics.png")
    politicsButton = Button(
        root2,
        image=img10,
        bg="#66b3ff",
        relief="raised",
        command=politicsClick,
        border=0,
    )
    politicsButton.place(x=500, y=445)
    politics = Label(
        root2,
        text="Politics",
        bg="#66b3ff",
        font="Cambria",
    )
    politics.place(x=500, y=515)

    root2.mainloop()


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
root.mainloop()
