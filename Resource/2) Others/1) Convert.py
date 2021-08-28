# Converts 20 questions inserted, into 20 list of Question and choices within a single parent list.

from tkinter import messagebox

try:

    total_list = []

    for i in range(1, 21):
        # The comments below shows what happens in one iteration.

        inp = input(f"Enter {i} : ")  # Question  A. Answer(choice)  B. Choice_1 C. Choice_2 D. Choice_3

        # Make sure to add something unique and possibly least used sequence of random characters.
        # There were errors when ',' was used;
        # When commas ',' were already in the question and it created more than 5 elements.

        b = inp.replace('A.', 'zzzzz')  # Question  zzzzz Answer(choice)  B. Choice_1 C. Choice_2 D. Choice_3
        c = b.replace('B.', 'zzzzz')  # Question  zzzzz Answer(choice)  zzzzz Choice_1 C. Choice_2 D. Choice_3
        d = c.replace('C.', 'zzzzz')  # Question  zzzzz Answer(choice)  zzzzz Choice_1 zzzzz Choice_2 D. Choice_3
        e = d.replace('D.', 'zzzzz')  # Question  zzzzz Answer(choice)  zzzzz Choice_1 zzzzz Choice_2 zzzzz Choice_3

        # Its okay if there are only 2 or 3 choices.
        # This is taken care of in the question.py program.

        list_individual = e.split("zzzzz")  # ['Question  ', ' Anser(choice)  ', ' Choice_1 ', ' Choice_2 ', ' Choice_3']
        # 5 elements: Question, Answer, Option_1, Option_2, Option_3

        total_list.append(list_individual)  # [['Question  ', ' Anser(choice)  ', ' Choice_1 ', ' Choice_2 ', ' Choice_3']]

    print(total_list)  # Prints a single list of 20 MCQs lists.

except BaseException as er:
    messagebox.showerror("Error", str(type(er))[6:-1] + " : " + str(er))