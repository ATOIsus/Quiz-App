import _tkinter
from tkinter import *
from tkinter import messagebox
root=Tk()

class signin:
    def __init__(self,root):
        self.root=root
        self.root.title("SIGN IN")
        self.root.geometry("700x500")
        self.root.iconbitmap("user.ico")
        self.root.configure(bg="#404040")

        frame=Frame(self.root,bg="white")
        frame.place(x=150,y=150,height=300,width=400)

        s_in=Label(frame,text="Sign In",font=("Times",30,"bold"),fg="green",bg="white")
        s_in.place(x=60,y=30)

        user_n=Label(frame,text="Username",font=("arial",15,"bold"),fg="green",bg="white")
        user_n.place(x=60,y=90)
        self.entry1=Entry(frame,font=("arial,15"),bg="light green")
        self.entry1.place(x=60,y=120,width="300",height="30")

        p_word = Label(frame, text="Password", font=("arial", 15, "bold"), fg="green", bg="white")
        p_word.place(x=60, y=160)
        self.entry2 = Entry(frame, font=("arial,15"), bg="light green",show="*")
        self.entry2.place(x=60, y=190, width="300", height="30")

        btn=Button(frame,text="sign in",bd=4,bg="green",fg="white",font=("arial",15),command=self.signn)
        btn.place(x=160,y=240)

        btn1 = Button(self.root, text="SIGN UP", bd=4, bg="blue", fg="white", font=("arial", 15), command=self.sign_wn1)
        btn1.place(x=580, y=440)

    def sign_wn(self):
        self.root.destroy()

    def signn(self):
        if self.entry1.get() == "" or self.entry2.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            messagebox.showinfo("Congrats","You are signned in",parent=self.root)

    def __init__1(self,root):
        self.root=root
        self.root.title("SIGN UP")
        self.root.geometry("700x500")
        self.root.iconbitmap("user.ico")
        self.root.configure(bg="#404040")

        frame=Frame(self.root,bg="white")
        frame.place(x=150,y=150,height=320,width=400)

        s_up=Label(frame,text="Sign Up",font=("Times",30,"bold"),fg="green",bg="white")
        s_up.place(x=60,y=5)

        u_name=Label(frame,text="Username",font=("arial",15,"bold"),fg="green",bg="white")
        u_name.place(x=60,y=53)
        self.entry0=Entry(frame,font=("arial,15"),bg="light green")
        self.entry0.place(x=60,y=80,width="300",height="30")

        email = Label(frame, text="E-mail", font=("arial", 15, "bold"), fg="green", bg="white")
        email.place(x=60, y=110)
        self.entry1 = Entry(frame, font=("arial,15"), bg="light green")
        self.entry1.place(x=60, y=140, width="300", height="30")

        password = Label(frame, text="Password", font=("arial", 15, "bold"), fg="green", bg="white")
        password.place(x=60, y=170)
        self.entry2 = Entry(frame, font=("arial,15"), bg="light green",show="*")
        self.entry2.place(x=60, y=200, width="300", height="30")

        c_password = Label(frame, text="Confirm Password", font=("arial", 15, "bold"), fg="green", bg="white")
        c_password.place(x=60, y=230)
        self.entry3 = Entry(frame, font=("arial,15"), bg="light green",show="*")
        self.entry3.place(x=60, y=260, width="300", height="30")

        btn=Button(self.root,text="sign up",bd=3,bg="green",fg="white",font=("arial",15),command=self.signn1)
        btn.place(x=300,y=450)

        btn1 = Button(self.root, text="SIGN IN", bd=4, bg="blue", fg="white", font=("arial", 15), command=self.sign_wn)
        btn1.place(x=580, y=440)

    def sign_wn1(self):
        self.root.destroy()



    def signn1(self):
        if self.entry0.get() == "" or self.entry1.get() == ""  or self.entry2.get() == "" or self.entry3.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif  (self.entry2.get()) != (self.entry3.get()):
            messagebox.showerror("Error", "Password Unmatched", parent=self.root)
        else:
            messagebox.showinfo("Congrats","You are signned up",parent=self.root)

obj = signin(root)
root.mainloop()