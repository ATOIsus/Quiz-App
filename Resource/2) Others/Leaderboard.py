from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import sqlite3



root = Tk()
root.title('Database')
root.geometry('700x700')
# root.resizable(False, False)


# region Global variables.

global quiz_topic
global score
global PlayerID
global db_score
global username_var
global password_var

img = Image.open('Images/bg.jpg')
resized_img = img.resize((600, 600), Image.ANTIALIAS)
converted_img = ImageTk.PhotoImage(resized_img)

# endregion


# region Create Database & Table.

# Creating the table

conn = sqlite3.connect('Player Database.db')

c = conn.cursor()

c.execute(""" CREATE TABLE IF NOT EXISTS
          information
          (
          Name text, 
          Username text,
          Password text,
          Architecture integer, 
          Lab integer,
          Math integer,
          Politics integer,
          Programming integer,
          Science integer,
          Sport integer,
          GK integer
          )""")

conn.commit()
conn.close()

# endregion



# region Entry.

name_ent = Entry(root, width=30)
name_ent.grid(row=1, column=1, padx=20)

uname_ent = Entry(root, width=30)
uname_ent.grid(row=2, column=1)

password_ent = Entry(root, width=30)
password_ent.grid(row=3, column=1)

# endregion



# region Labels.

name_lbl = Label(root, text="Name")
name_lbl.grid(row=1, column=0)

uname_lbl = Label(root, text="Username")
uname_lbl.grid(row=2, column=0)

password_lbl = Label(root, text="Password")
password_lbl.grid(row=3, column=0)

# endregion



# region Submit Function.



def submit_fun():

    conn1 = sqlite3.connect('Player Database.db')
    c1 = conn1.cursor()

    c1.execute("INSERT INTO information VALUES (:Name, :Username, :Password, :Architecture, :Lab , :Math , :Politics , :Programming , :Science , :Sport, :GK)",
              {
                  'Name': name_ent.get(),
                  'Username': uname_ent.get(),
                  'Password': password_ent.get(),
                  'Architecture': 0,
                  'Lab': 0,
                  'Math': 0,
                  'Politics': 0,
                  'Programming': 0,
                  'Science': 0,
                  'Sport': 0,
                  'GK': 0,
              })

    messagebox.showinfo("Completed", "Record Inserted")

    conn1.commit()
    conn1.close()

    name_ent.delete(0, END)
    uname_ent.delete(0, END)
    password_ent.delete(0, END)


# Creating submit button.


submit_btn = Button(root, text="Add Records", command=submit_fun)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


# endregion



# region Query Function.



def query_fun():

    global converted_img
    global quiz_topic
    quiz_topic = input("Enter the subject:  ")

    conn2 = sqlite3.connect('Player Database.db')
    c2 = conn2.cursor()

    c2.execute(f"""SELECT ROWID, Name, Username, {quiz_topic}  FROM information 
                    ORDER BY {quiz_topic} DESC
                    LIMIT 10;""")
    rows = c2.fetchall()

    root.wm_attributes('-transparentcolor', '#AE9152')

    frm = LabelFrame(root, text="Leaderboard", font = ("Futura" , 25), fg = "gold", labelanchor = 'n',  relief="raised",
                     bd = 15, bg = '#AE9152', height = 600, width = 600)
    frm.grid(row=9, column=0)

    lbl_img = Label(frm, image = converted_img)
    lbl_img.grid(padx = 50, pady = 50)

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview",
                    background="orange",
                    font=("Futura", 15))
    style.map('Treeview', background=[('selected', 'Black')], foreground =[('selected', 'red')])

    style.configure("Treeview.Heading", background = "black", foreground = "gold", font=("Futura", 15))
    # style.map('Treeview.Heading', background = [('selected', 'white')])


    tv = ttk.Treeview(lbl_img, column=(1, 2, 3, 4), show="headings", height=10)
    tv.grid(padx = 10, pady = 10)

    tv.column(1, width=50,  stretch=False)
    tv.column(2, width=185, stretch=False)
    tv.column(3, width=200, stretch=False)
    tv.column(4, width=120, stretch=False)

    tv.heading(1, text="ID")
    tv.heading(2, text="Name")
    tv.heading(3, text="Username")
    tv.heading(4, text=f"{quiz_topic}")

    for i in rows:
        tv.insert("", "end", values=i)

    conn2.commit()
    conn2.close()



query_btn = Button(root, text="Show Records", command=query_fun)
query_btn.grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

# endregion



# region Delete Function.

delete_lbl = Label(root, text="Player ID")
delete_lbl.grid(row=12, column=0, pady=5)

delete_ent = Entry(root, width=30)
delete_ent.grid(row=12, column=1, pady=5)


def delete_fun():

    conn3 = sqlite3.connect('Player Database.db')
    c3 = conn3.cursor()

    c3.execute(f"DELETE from information WHERE ROWID = {delete_ent.get()}")

    conn3.commit()
    conn3.close()

    delete_ent.delete(0, END)

    query_fun()


delete_btn = Button(root, text="Delete", command=delete_fun)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=120)

# endregion



# region Sign In.



def signin_fun():

    global username_var
    global password_var
    global quiz_topic
    global PlayerID
    global db_score

    quiz_topic   = input("Enter the subject: ")
    username_var = input("Enter Username: ")
    password_var = input("Enter Password: ")

    conn4 = sqlite3.connect('Player Database.db')
    c4 = conn4.cursor()

    c4.execute(f"SELECT ROWID, Username, Password, {quiz_topic} FROM information")
    records = c4.fetchall()


    for record in records:

        if username_var == str(record[1]) and password_var == str(record[2]):
            PlayerID = record[0]
            db_score = record[3]
            print(f'PlayerID {PlayerID}')
            print(f'Db_score {db_score}')
            break
        else:
            pass
    else:
        messagebox.showerror('Error', 'Wrong Username or Password')

    conn4.commit()
    conn4.close()


signin_btn = Button(root, text="Sign In", command=signin_fun)
signin_btn.grid(row=13, column=0, columnspan=2, pady=10, padx=10, ipadx=120)


# endregion




# region Update Function.



def update_fun():

    global db_score
    global score

    score = int(input("Enter the score: "))

    if score > db_score :

        conn5 = sqlite3.connect('Player Database.db')
        c5 = conn5.cursor()

        c5.execute(f"UPDATE information SET {quiz_topic} = ? where ROWID = ?", (score, PlayerID))

        conn5.commit()
        conn5.close()

    else:
        pass


update_btn = Button(root, text="Update", command=update_fun)
update_btn.grid(row=15, column=0, columnspan=2, pady=10, padx=10, ipadx=120)


# endregion



root.mainloop()