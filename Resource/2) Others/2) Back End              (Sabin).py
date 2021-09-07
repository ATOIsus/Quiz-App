from tkinter import *
from tkinter import messagebox

global ent_uname_in, ent_pass_in
global ent_uname_up, ent_email_up, ent_pass_up, ent_c_pass_up


# region Sign In (Bishal).


def sign_in():

    global ent_uname_in, ent_pass_in

    if ent_uname_in.get() == "" or ent_pass_in.get() == "":
        messagebox.showerror("Error", "All fields are required")

    else:
        messagebox.showinfo("Congrats", "You are signed in")

        ent_uname_in.delete(0, END)
        ent_pass_in.delete(0, END)


def sign_in_GUI():

    try:
        frame_signup.destroy()
    except e:
        print(e)

    global frame_signin
    global ent_uname_in, ent_pass_in


    frame_signin = LabelFrame(root, bg="white", bd=0, height=400, width=450)
    frame_signin.place(x=150, y=110)

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

    btn_signin_in = Button(frame_signin, text="Sign In", bd=4, bg="green", fg="white", font=("arial", 15), command=sign_in)
    btn_signin_in.place(x=160, y=240)

    btn_signup_in = Button(frame_signin, text="SIGN UP", bd=4, bg="blue", fg="white", font=("arial", 15), command=sign_up_GUI)
    btn_signup_in.place(x=350, y=350)


#  endregion



# region Sign Up (Bishal).



def sign_up():

    global ent_uname_up, ent_email_up, ent_pass_up, ent_c_pass_up

    if ent_uname_up.get() == "" or ent_email_up.get() == "" or ent_pass_up.get() == "" or ent_c_pass_up.get() == "":
        messagebox.showerror("Error", "All fields are required")

    elif (ent_pass_up.get()) != (ent_c_pass_up.get()):
        messagebox.showerror("Error", "Password Unmatched")

    else:
        messagebox.showinfo("Congrats", "You are signed up")

        ent_uname_up.delete(0, END)
        ent_email_up.delete(0, END)
        ent_pass_up.delete(0, END)
        ent_c_pass_up.delete(0, END)



def sign_up_GUI():
    try:
        frame_signin.destroy()
    except e:
        print(e)

    global frame_signup
    global ent_uname_up, ent_email_up, ent_pass_up, ent_c_pass_up

    frame_signup = LabelFrame(root, bg="white", bd=0, height=400, width=450)
    frame_signup.place(x=150, y=110)


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
    ent_pass_up = Entry(frame_signup, font="arial,15", bg="light green", show="*")
    ent_pass_up.place(x=60, y=200, width="300", height="30")

    lbl_c_pass = Label(frame_signup, text="Confirm Password", font=("arial", 15, "bold"), fg="green", bg="white")
    lbl_c_pass.place(x=60, y=230)
    ent_c_pass_up = Entry(frame_signup, font="arial,15", bg="light green", show="*")
    ent_c_pass_up.place(x=60, y=260, width="300", height="30")

    btn_signup_up = Button(frame_signup, text="Sign Up", bd=3, bg="green", fg="white", font=("arial", 15), command=sign_up)
    btn_signup_up.place(x=160, y=310)

    btn_signin_up = Button(frame_signup, text="SIGN IN", bd=4, bg="blue", fg="white", font=("arial", 15), command=sign_in_GUI)
    btn_signin_up.place(x=350, y=350)


# endregion


root = Tk()
root.title("SIGN IN")
root.geometry("750x600")
root.iconbitmap("user.ico")
root.configure(bg="#404040")
frame_signin = LabelFrame(root, bg="white", bd=0, height=400, width=450)
frame_signup = LabelFrame(root, bg="white", bd=0, height=400, width=450)

sign_up_GUI()


root.mainloop()



# Compiled and Managed by Sabin Maharjan.