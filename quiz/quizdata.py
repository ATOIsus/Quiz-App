from tkinter import *
import sqlite3

root = Tk()
root.title(" DataBase Record ")
root.geometry("400x600")
'''
# Create a Database or connect to one
conn=sqlite3.connect('address_book.db')
# Create cursor
c = conn.cursor()

# Create a Table
c.execute("""CREATE TABLE addresses(
            name text,
            user_name text,
            email text,
            password text,) """)
'''


def update():
    # Create a Database or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()
    record_id = delete_box.get()
    c.execute("""
                UPDATE addresses SET 
                 name = :name,
                 user_name = :user_name,
                 email = :email,
                 password = :password,


                WHERE oid = :oid""",
              {
                  'name': name_edit.get(),
                  'user_name': user_name_edit.get(),
                  'email': email_edit.get(),
                  'password': password_edit.get(),

                  'oid': record_id
              })
    # commit changes
    conn.commit()
    # close connection
    conn.close()


# create edit() function to update a record
def edit():
    editor = Tk()
    editor.title("Update a Record")
    editor.geometry("400x600")
    root.iconbitmap('edit.ico')
    # Create a Database or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()
    record_id = delete_box.get()
    # Query the Data base
    c.execute(" SELECT * FROM addresses WHERE oid =" + record_id)
    records = c.fetchall()

    show = ''
    for record in records[0:]:
        show += str(record) + "\t" + "\n"

        # Create Global variable for text boxes name
        global name_edit
        global user_name_edit
        global email_edit
        global password_edit

        # Create Text Boxes
        name_edit = Entry(editor, width=50)
        name_edit.grid(row=0, column=1, padx=20, pady=5)
        user_name_edit = Entry(editor, width=50)
        user_name_edit.grid(row=1, column=1, padx=20, pady=5)
        email_edit = Entry(editor, width=50)
        email_edit.grid(row=2, column=1, padx=20, pady=5)
        password_edit = Entry(editor, width=50)
        password_edit.grid(row=3, column=1, padx=20, pady=5)

        # Create Text Label
        name_label_edit = Label(editor, text=" Name")
        name_label_edit.grid(row=0, column=0)
        user_name_label_edit = Label(editor, text="user_Name")
        user_name_label_edit.grid(row=1, column=0)
        email_label_edit = Label(editor, text="email")
        email_label_edit.grid(row=2, column=0)
        password_label_edit = Label(editor, text="password")
        password_label_edit.grid(row=3, column=0)

        # Create a Save Button to save edited record
        save_btn = Button(editor, text=" save Record ", command=update)
        save_btn.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

        # loop through result
        for record in records:
            name_edit.insert(0, record[0])
            user_name_edit.insert(0, record[0])
            email_edit.insert(0, record[0])
            password_edit.insert(0, record[0])


# Create data base submit function
def submit():
    # Create a Database or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()
    # Insert into Table
    c.execute(" INSERT INTO addresses VALUES (:name, :user_name, :email, :password) ",
              {
                  'name': name.get(),
                  'user_name': user_name.get(),
                  'email': email.get(),
                  'password': password.get()

              })

    # commit changes
    conn.commit()
    # close connection
    conn.close()

    # clear the boxes
    name.delete(0, END)
    user_name.delete(0, END)
    email.delete(0, END)
    password.delete(0, END)


# Create a function to show record
def query():
    # Create a Database or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()

    # Query the Data base
    c.execute(" SELECT *,oid FROM addresses ")
    records = c.fetchall()
    show = ''
    for record in records[0:]:
        show += str(record[0:6]) + "\t" + str(record[6]) + "\n"

    query_label = Label(root, text=show)
    query_label.grid(row=12, column=0, columnspan=2)

    # commit changes
    conn.commit()
    # close connection
    conn.close()


# create a function to delete record
def delete():
    # Create a Database or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    c = conn.cursor()

    # delete a record
    c.execute("DELETE from addresses WHERE oid=" + delete_box.get())
    # commit changes
    conn.commit()
    # close connection
    conn.close()


# Create Text Boxes
name = Entry(root, width=50)
name.grid(row=0, column=1, padx=20, pady=5)
user_name = Entry(root, width=50)
user_name.grid(row=1, column=1, padx=20, pady=5)
email = Entry(root, width=50)
email.grid(row=2, column=1, padx=20, pady=5)
password = Entry(root, width=50)
password.grid(row=3, column=1, padx=20, pady=5)
delete_box = Entry(root, width=50)
delete_box.grid(row=4, column=1, padx=20, pady=5)

# Create Text Label
name_label = Label(root, text=" Name")
name_label.grid(row=0, column=0)
user_name_label = Label(root, text="User_Name")
user_name_label.grid(row=1, column=0)
email_label = Label(root, text="Email")
email_label.grid(row=2, column=0)
password_label = Label(root, text="Password")
password_label.grid(row=3, column=0)

delete_box_label = Label(root, text="Enter ID")
delete_box_label.grid(row=4, column=0)

# Create Submit Button
submit_btn = Button(root, text='Submit', command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=120)

# Create Query Button
query_btn = Button(root, text=" Show Records ", command=query)
query_btn.grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

# Create Delete Button
delete_btn = Button(root, text=" Delete Record ", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

# Create Update Button
edit_btn = Button(root, text=" Edit Record ", command=edit)
edit_btn.grid(row=11, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

'''
# commit changes
conn.commit()
# close connection
conn.close()
'''
root.mainloop()



