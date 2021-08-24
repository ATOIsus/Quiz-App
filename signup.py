from tkinter import *
from tkinter import messagebox
root=Tk()

class sign:
    def __init__(self,root):
        self.root=root
        self.root.title("SIGN UP")
        self.root.geometry("700x500")
        self.root.iconbitmap("user.ico")
        self.root.configure(bg="#00cccc")

        frame=Frame(self.root,bg="white")
        frame.place(x=150,y=150,height=320,width=400)

        lbl=Label(frame,text="Sign Up",font=("Times",30,"bold"),fg="green",bg="white")
        lbl.place(x=60,y=5)

        lbl0=Label(frame,text="Username",font=("arial",15,"bold"),fg="green",bg="white")
        lbl0.place(x=60,y=53)
        self.entry0=Entry(frame,font=("arial,15"),bg="light green")
        self.entry0.place(x=60,y=80,width="300",height="30")

        lbl1 = Label(frame, text="E-mail", font=("arial", 15, "bold"), fg="green", bg="white")
        lbl1.place(x=60, y=110)
        self.entry1 = Entry(frame, font=("arial,15"), bg="light green")
        self.entry1.place(x=60, y=140, width="300", height="30")

        lbl2 = Label(frame, text="Password", font=("arial", 15, "bold"), fg="green", bg="white")
        lbl2.place(x=60, y=170)
        self.entry2 = Entry(frame, font=("arial,15"), bg="light green",show="*")
        self.entry2.place(x=60, y=200, width="300", height="30")

        lbl3 = Label(frame, text="Confirm Password", font=("arial", 15, "bold"), fg="green", bg="white")
        lbl3.place(x=60, y=230)
        self.entry3 = Entry(frame, font=("arial,15"), bg="light green",show="*")
        self.entry3.place(x=60, y=260, width="300", height="30")

        btn=Button(self.root,text="sign up",bd=3,bg="green",fg="white",font=("arial",15),command=self.signn)
        btn.place(x=300,y=450)

    def signn(self):
        if self.entry0.get() == "" or self.entry1.get() == ""  or self.entry2.get() == "" or self.entry3.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif  (self.entry2.get()) != (self.entry3.get()):
            messagebox.showerror("Error", "Password Unmatched", parent=self.root)
        else:
            messagebox.showinfo("Congrats","You are signned up",parent=self.root)

obj = sign(root)
root.mainloop()