from tkinter import *
from tkinter import messagebox
root=Tk()

class sign:
    def __init__(self,root):
        self.root=root
        self.root.title("SIGN IN")
        self.root.geometry("700x500")
        self.root.iconbitmap("user.ico")
        self.root.configure(bg="#00cccc")

        frame=Frame(self.root,bg="white")
        frame.place(x=150,y=150,height=300,width=400)

        lbl=Label(frame,text="Sign In",font=("Times",30,"bold"),fg="green",bg="white")
        lbl.place(x=60,y=30)

        lbl1=Label(frame,text="Username",font=("arial",15,"bold"),fg="green",bg="white")
        lbl1.place(x=60,y=90)
        self.entry1=Entry(frame,font=("arial,15"),bg="light green")
        self.entry1.place(x=60,y=120,width="300",height="30")

        lbl2 = Label(frame, text="Password", font=("arial", 15, "bold"), fg="green", bg="white")
        lbl2.place(x=60, y=160)
        self.entry2 = Entry(frame, font=("arial,15"), bg="light green",show="*")
        self.entry2.place(x=60, y=190, width="300", height="30")

        btn=Button(frame,text="sign in",bd=4,bg="green",fg="white",font=("arial",15),command=self.signn)
        btn.place(x=160,y=240)

    def signn(self):
        if self.entry1.get() == "" or self.entry2.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            messagebox.showinfo("Congrats","You are signned in",parent=self.root)

obj = sign(root)
root.mainloop()