from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import sqlite3


root = Tk()
root.title('Database')
root.geometry('750x600')
# root.resizable(False, False)


try:

    # region Images.

    img = Image.open('Images/lava.jpg')
    resized_img = img.resize((650, 440), Image.ANTIALIAS)
    converted_img = ImageTk.PhotoImage(resized_img)

    img1 = Image.open('Images/lines.jpg')
    resized_img1 = img1.resize((610, 400), Image.ANTIALIAS)
    converted_img1 = ImageTk.PhotoImage(resized_img1)


    # endregion



    # region Query Function.



    def query_fun():

        global converted_img
        global converted_img1

        quiz_topic = input("Enter the subject:  ")

        conn = sqlite3.connect('Player Database.db')
        cur = conn.cursor()

        cur.execute(f"""SELECT ROWID, Name, Username, {quiz_topic}  FROM information 
                        ORDER BY {quiz_topic} DESC
                        LIMIT 10;""")
        rows = cur.fetchall()

        root.wm_attributes('-transparentcolor', '#AE9152')

        frm = LabelFrame(root, text="Leaderboard", font=('Helvetica', 34, 'bold italic'), fg = "gold", labelanchor = 'n',  relief="raised",
                         bd = 15, bg = '#AE9152', height = 550, width = 750)
        frm.grid(row=9, column=1)

        lbl_img = Label(frm, image = converted_img, height = 440, width = 650, bd = 0)
        lbl_img.place(x = 30, y = 10)

        lbl_img1 = Label(lbl_img, image = converted_img1, height = 400, width = 610, bd = 0)
        lbl_img1.place(x = 23, y = 25)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview",
                        rowheight = 30,
                        background="black",
                        foreground = "#FFD700",
                        font=('Helvetica', 14, 'bold italic'))
        style.map('Treeview', background=[('selected', 'Black')], foreground =[('selected', 'red')])

        style.configure("Treeview.Heading", background = "black", foreground = "gold", font=('Helvetica', 14, 'bold italic'))
        style.map('Treeview.Heading', background = [('selected', 'red')])


        tv = ttk.Treeview(lbl_img1, column=(1, 2, 3, 4), show="headings", height=10)
        tv.place(x = 13, y = 33)

        tv.column(1, width=50,  stretch=False)
        tv.column(2, width=190, stretch=False)
        tv.column(3, width=205, stretch=False)
        tv.column(4, width=135, stretch=False)

        tv.heading(1, text="ID")
        tv.heading(2, text="Name")
        tv.heading(3, text="Username")
        tv.heading(4, text=f"{quiz_topic}")

        for i in rows:
            tv.insert("", "end", values=i)

        conn.commit()
        conn.close()


    query_btn = Button(root, text="Leaderboard", command=query_fun)
    query_btn.grid(columnspan=2, padx=10, pady=10, ipadx=100)

    # endregion


except BaseException as er:
    messagebox.showerror("Error", str(type(er))[6:-1] + " : " + str(er))
    root.destroy()


else:
    root.mainloop()