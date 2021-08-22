



all = []

for i in range(1, 21):

    inp = input(f"Enter {i} : ")

    b = inp.replace('A.', ',')
    c = b.replace('B.', ',')
    d = c.replace('C.', ',')
    e = d.replace('D.', ',')

    list_1 = e.split(",")
    all.append(list_1)



print(all)


