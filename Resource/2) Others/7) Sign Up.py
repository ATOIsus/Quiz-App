from tkinter import *
from tkinter import messagebox
import sqlite3



root = Tk()
root.title('Sign Up')
root.geometry('300x130')
root.resizable(False, False)


# region Global variables.

global quiz_topic
global score
global playerID
global db_score
global username_var
global password_var


# endregion



# region Create Database & Table.

# Creating the table

conn = sqlite3.connect('Database/Player Database.db')

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

password_ent = Entry(root, width=30, show = "*")
password_ent.grid(row=3, column=1)

confirm_password_ent = Entry(root, width=30, show = "*")
confirm_password_ent.grid(row=4, column=1)

# endregion



# region Labels.

name_lbl = Label(root, text="Name")
name_lbl.grid(row=1, column=0)

uname_lbl = Label(root, text="Username")
uname_lbl.grid(row=2, column=0)

password_lbl = Label(root, text="Password")
password_lbl.grid(row=3, column=0)

confirm_password_lbl = Label(root, text="C. Password")
confirm_password_lbl.grid(row=4, column=0)

# endregion



# region Submit Function.

try:

    def submit_fun():

        if uname_ent.get() == '' and password_ent.get() == '' and name_ent.get() == '' :
            messagebox.showerror("Error!", "Cannot Enter Empty Fields!")

        elif name_ent.get() == '':
            messagebox.showerror("Error!", "Cannot Enter Empty Name!")

        elif uname_ent.get() == '':
            messagebox.showerror("Error!", "Cannot Enter Empty Username!")

        elif password_ent.get() == '':
            messagebox.showerror("Error!", "Cannot Enter Empty Password!")

        elif password_ent.get() != confirm_password_ent.get():
            messagebox.showerror("Error!", "Password and Confirm Password need to be the same!")

        else:
            conn1 = sqlite3.connect('Database/Player Database.db')
            c1 = conn1.cursor()

            c1.execute(f"SELECT Username FROM information")
            records = c1.fetchall()


            for record in records:

                if uname_ent.get() == str(record[0]):
                    messagebox.showerror("Error!", "Cannot Use Same Username Twice!")
                    break

                else:
                    pass

            else:
                c1.execute(
                    """INSERT INTO information VALUES (:Name, :Username, :Password, :Architecture, 
                    :Lab , :Math , :Politics , :Programming , :Science , :Sport, :GK)""",
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
            confirm_password_ent.delete(0, END)


    # Creating submit button.


    submit_btn = Button(root, text="Sign Up", command=submit_fun)
    submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


# endregion


except BaseException as er:
    messagebox.showerror("Error", str(type(er))[6:-1] + " : " + str(er))
    root.destroy()


else:
    root.mainloop()