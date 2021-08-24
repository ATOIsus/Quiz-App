from tkinter import *
from tkinter import messagebox
import sqlite3
from tkinter import ttk

root = Tk()
root.title('Database')
root.geometry('500x550')
# root.resizable(False, False)



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


    conn4 = sqlite3.connect('Player Database.db')
    c4 = conn4.cursor()

    quiz_topic = input("Enter the subject:  ")

    c4.execute(f"SELECT ROWID, Name, Username, {quiz_topic}  FROM information")
    rows = c4.fetchall()

    frm = Frame(root)
    frm.grid(padx=20)

    tv = ttk.Treeview(frm, column=(1, 2, 3, 4), show="headings", height=5)
    tv.pack()

    tv.heading(1, text="Row ID")
    tv.heading(2, text="Name")
    tv.heading(3, text="Username")
    tv.heading(4, text="Score")


    for i in rows:
        tv.insert("", "end", values=i)

    conn4.commit()
    conn4.close()


query_btn = Button(root, text="Show Records", command=query_fun)
query_btn.grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

# endregion


# region Delete Function.

delete_lbl = Label(root, text="Player ID")
delete_lbl.grid(row=9, column=0, pady=5)

delete_ent = Entry(root, width=30)
delete_ent.grid(row=9, column=1, pady=5)


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








root.mainloop()
