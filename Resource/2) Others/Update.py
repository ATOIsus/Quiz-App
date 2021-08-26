from tkinter import *
from tkinter import messagebox
import sqlite3


root = Tk()
root.title('Update')
root.geometry('220x100')
root.resizable(False, False)


global username_var
global password_var
global quiz_topic
global PlayerID
global db_score



try:

    # region Sign In.

    def signin_fun():

        global username_var
        global password_var
        global quiz_topic
        global PlayerID
        global db_score

        try:

            quiz_topic   = input("Enter the subject: ")
            username_var = input("Enter Username: ")
            password_var = input("Enter Password: ")

            conn = sqlite3.connect('Player Database.db')
            cur = conn.cursor()

            cur.execute(f"SELECT ROWID, Username, Password, {quiz_topic} FROM information")
            records = cur.fetchall()


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

            conn.commit()
            conn.close()

        except BaseException as er:
            messagebox.showerror("Error while signing in", str(type(er))[6:-1] + " : " + str(er))


    signin_btn = Button(root, text="Sign In", command=signin_fun)
    signin_btn.grid(pady=10, padx=10, ipadx=60)


    # endregion


    # region Update Function.



    def update_fun():

        global db_score

        try:
            
            score = int(input("Enter the score: "))
    
            if score > db_score :
    
                conn1 = sqlite3.connect('Player Database.db')
                cur1 = conn1.cursor()
    
                cur1.execute(f"UPDATE information SET {quiz_topic} = ? where ROWID = ?", (score, PlayerID))
            
                conn1.commit()
                conn1.close()
    
            else:
                pass

        except BaseException as er1:
            messagebox.showerror("Error in update function", str(type(er1))[6:-1] + " : " + str(er1))


    update_btn = Button(root, text="Update", command=update_fun)
    update_btn.grid(pady=10, padx=10, ipadx=60)


    # endregion


except BaseException as er2:
    messagebox.showerror("Error within whole try block", str(type(er2))[6:-1] + " : " + str(er2))
    root.destroy()


else:
    root.mainloop()