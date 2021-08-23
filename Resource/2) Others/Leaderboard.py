from tkinter import *
import sqlite3
from tkinter import messagebox

root = Tk()
root.title('Database')

'''
# Creating the table

conn = sqlite3.connect('playerData.db')  

c = conn.cursor()


c.execute(""" CREATE TABLE information(
          Name text, 
          Username text,
          Password text,
          Score integer
          )""")


conn.commit()
conn.close()
'''

# Creating text boxes.

name_ent = Entry(root, width=30)
name_ent.grid(row=0, column=1, padx=20)

uname_ent = Entry(root, width=30)
uname_ent.grid(row=1, column=1)

password_ent = Entry(root, width=30)
password_ent.grid(row=2, column=1)

# Creating textbox labels.

name_lbl = Label(root, text="Name")
name_lbl.grid(row=0, column=0)

uname_lbl = Label(root, text="Username")
uname_lbl.grid(row=1, column=0)

password_lbl = Label(root, text="Password")
password_lbl.grid(row=2, column=0)


# Submit region

def submit_fun():
    conn = sqlite3.connect('playerData.db')
    c = conn.cursor()

    c.execute("INSERT INTO information VALUES (:Name, :Username, :Password, :Score)",
              {
                  'Name': name_ent.get(),
                  'Username': uname_ent.get(),
                  'Password': password_ent.get(),
                  'Score': 0
              })

    messagebox.showinfo("Completed", "Record inserted")

    conn.commit()
    conn.close()


# Creating submit button.

submit_btn = Button(root, text="Add Records", command=submit_fun)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


# Submit region


# Show region

def query_fun():
    conn = sqlite3.connect('playerData.db')
    c = conn.cursor()

    c.execute("SELECT *, oid FROM information")

    records = c.fetchall()

    record_str = ''
    query_lbl = Label(root, text=record_str)
    query_lbl.grid(row=8, column=0, columnspan=2)

    for record in records:
        record_str += str(record[0]) + ' ' + str(record[1]) + ' ' + str(record[2]) + ' ' + str(record[3]) + '\n'

    query_lbl.configure(text=record_str)

    conn.commit()
    conn.close()


query_btn = Button(root, text="Show Records", command=query_fun)
query_btn.grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

# Show region


# Delete region

delete_lbl = Label(root, text="Delete ID")
delete_lbl.grid(row=9, column=0, pady=5)

delete_ent = Entry(root, width=30)
delete_ent.grid(row=9, column=1, pady=5)


def delete_fun():
    conn = sqlite3.connect('playerData.db')
    c = conn.cursor()

    c.execute("DELETE from information WHERE oid = " + delete_ent.get())

    conn.commit()
    conn.close()


delete_btn = Button(root, text="Delete", command=delete_fun)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=120)

# Delete region


root.mainloop()
