from tkinter import *              # To use basic functions and methods of tkinter.
from tkinter import messagebox     # To show popup messagebox.
import sqlite3                     # To connect to the database.


root = Tk()
root.title('Database')
root.geometry('300x100')
root.resizable(False, False)



try:

    # region Delete Function.

    delete_lbl = Label(root, text="ID")
    delete_lbl.grid(row=2, column=0, pady=5)

    delete_ent = Entry(root, width=30)
    delete_ent.grid(row=2, column=1, pady=5)


    def delete_fun():

        """ Deletes the row with the given ID,
        but while implementing it will delete the row of the current user only (Get ROWID in sign in function).  """

        try:
            conn3 = sqlite3.connect('Database/Player Database.db')
            c3 = conn3.cursor()

            c3.execute(f"DELETE from information WHERE ROWID = {delete_ent.get()}")

            conn3.commit()
            conn3.close()

            delete_ent.delete(0, END)

            messagebox.showinfo("Success", "Account deleted!")

        except BaseException as er:
            messagebox.showerror("Error in Delete Function!", str(type(er))[6:-1] + " : " + str(er))



    delete_btn = Button(root, text="Delete", command=delete_fun)
    delete_btn.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=120)

    # endregion


except BaseException as er1:
    messagebox.showerror("Error", str(type(er1))[6:-1] + " : " + str(er1))
    root.destroy()


else:
    root.mainloop()