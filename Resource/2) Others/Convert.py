# Converts 20 questions inserted, into list of Question and choices within a parent list.


total_list = []

for i in range(1, 21):

    inp = input(f"Enter {i} : ")   # Question  A. Answer(choice)  B. Choice_1 C. Choice_2 D. Choice_3

    b = inp.replace('A.', ',')     # Question  , Answer(choice)  B. Choice_1 C. Choice_2 D. Choice_3
    c = b.replace('B.', ',')       # Question  , Answer(choice)  , Choice_1 C. Choice_2 D. Choice_3
    d = c.replace('C.', ',')       # Question  , Answer(choice)  , Choice_1 , Choice_2 D. Choice_3
    e = d.replace('D.', ',')       # Question  , Answer(choice)  , Choice_1 , Choice_2 , Choice_3

    list_individual = e.split(",")      # ['Question  ', ' Anser(choice)  ', ' Choice_1 ', ' Choice_2 ', ' Choice_3']
    total_list.append(list_individual)  # [['Question  ', ' Anser(choice)  ', ' Choice_1 ', ' Choice_2 ', ' Choice_3']]

print(total_list)