import _tkinter
from tkinter import *
from tkinter import messagebox, Tk




def sign_up():
    if ent_uname_up.get() == "" or ent_email_up.get() == "" or entry_pass_up.get() == "" or ent_c_pass_up.get() == "":
        messagebox.showerror("Error", "All fields are required")
        
    elif (entry2.get()) != (entry3.get()):
        messagebox.showerror("Error", "Password Unmatched")
        
    else:
        messagebox.showinfo("Congrats", "You are signed up")


def sign_in():
    if ent_uname_in.get() == "" or ent_pass_in.get() == "":
        messagebox.showerror("Error", "All fields are required")

    else:
        messagebox.showinfo("Congrats", "You are signed in")



def sign_in_GUI():

    frame_signup.destroy()

    frame_signin.place(x=150, y=150, height=300, width=400, bg="#404040")


    lbl_signin = Label(frame_signin, text="Sign In", font=("Times", 30, "bold"), fg="green", bg="white")
    lbl_signin.place(x=60, y=30)

    lbl_user_n = Label(frame_signin, text="Username", font=("arial", 15, "bold"), fg="green", bg="white")
    lbl_user_n.place(x=60, y=90)
    ent_uname_in = Entry(frame_signin, font="arial, 15", bg="light green")
    ent_uname_in.place(x=60, y=120, width="300", height="30")

    lbl_p_word = Label(frame_signin, text="Password", font=("arial", 15, "bold"), fg="green", bg="white")
    lbl_p_word.place(x=60, y=160)
    ent_pass_in = Entry(frame_signin, font="arial, 15", bg="light green", show="*")
    ent_pass_in.place(x=60, y=190, width="300", height="30")

    btn_signin = Button(frame_signin, text="Sign In", bd=4, bg="green", fg="white", font=("arial", 15), command=sig_in)
    btn_signin.place(x=160, y=240)

    btn_signup = Button(frame_signin, text="SIGN UP", bd=4, bg="blue", fg="white", font=("arial", 15), command=sign_up_GUI)
    btn_signup.place(x=580, y=440)





def sign_up_GUI():

    frame_signin.destroy()

    frame_signup.place(x=150, y=150, height=320, width=400)


    lbl_signup = Label(frame_signup, text="Sign Up", font=("Times", 30, "bold"), fg="green", bg="white")
    lbl_signup.place(x=60, y=5)

    lbl_u_name = Label(frame_signup, text="Username", font=("arial", 15, "bold"), fg="green", bg="white")
    lbl_u_name.place(x=60, y=53)
    ent_uname_up = Entry(frame_signup, font="arial,15", bg="light green")
    ent_uname_up.place(x=60, y=80, width="300", height="30")

    lbl_email = Label(frame_signup, text="E-mail", font=("arial", 15, "bold"), fg="green", bg="white")
    lbl_email.place(x=60, y=110)
    ent_email_up = Entry(frame_signup, font="arial,15", bg="light green")
    ent_email_up.place(x=60, y=140, width="300", height="30")

    lbl_pass = Label(frame_signup, text="Password", font=("arial", 15, "bold"), fg="green", bg="white")
    lbl_pass.place(x=60, y=170)
    entry_pass_up = Entry(frame_signup, font="arial,15", bg="light green", show="*")
    entry_pass_up.place(x=60, y=200, width="300", height="30")

    lbl_c_pass = Label(frame_signup, text="Confirm Password", font=("arial", 15, "bold"), fg="green", bg="white")
    lbl_c_pass.place(x=60, y=230)
    ent_c_pass_up = Entry(frame_signup, font="arial,15", bg="light green", show="*")
    ent_c_pass_up.place(x=60, y=260, width="300", height="30")

    btn = Button(frame_signup, text="sign up", bd=3, bg="green", fg="white", font=("arial", 15), command=sign_up)
    btn.place(x=300, y=450)
    
    btn1 = Button(frame_signup, text="SIGN IN", bd=4, bg="blue", fg="white", font=("arial", 15), command=sign_in_GUI)
    btn1.place(x=580, y=440)



root = Tk()

root.title("SIGN IN")
root.geometry("700x500")
root.iconbitmap("user.ico")

frame_signin = Frame(root, bg="white")
frame_signup = Frame(root, bg="white")



sign_in_GUI()


root.mainloop()
