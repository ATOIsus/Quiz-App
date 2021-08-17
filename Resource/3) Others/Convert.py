



all = []

for i in range(20):

    a = input(f"Enter {i} : ")

    b = a.replace('a)', ',')
    c = b.replace('b)', ',')
    d = c.replace('c)', ',')
    e = d.replace('d)', ',')

    list_1 = e.split(",")
    all.append(list_1)



print(all)


