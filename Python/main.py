import datetime
from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage
import mysql.connector

mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                               database='LifechoicesOnline',
                               auth_plugin='mysql_native_password')
mycursor = mydb.cursor()

root = Tk()
root.title("Login")
root.geometry("2000x1000")
root.config(bg="#55a630")


class Login:
    def __init__(self, master):
        self.master = master
        self.master.title("Life Choices")

        self.master.bind('<Control-a>', self.admin)

        self.frame = Frame(self.master, border="1", width=400, height=400, relief="groove", borderwidth=1, bg="#ffffff")
        self.frame.place(relx="0.35", rely="0.2")

        logo = PhotoImage(file="/home/adam/Documents/Python/lc.png", master=self.master)
        logo = logo.subsample(2)
        self.lg = Label(self.frame, image=logo, bg="#007f5f", width="400", height="150")
        self.lg.place(relx="-0.01", rely="-0.01")

        self.signin = Label(self.frame, text="Sign in", font="Google-Sans 18", bg="White", fg="Black")
        self.signin.place(relx="0.38", rely="0.4")

        self.sub = Label(self.frame, text="Enter Your ID Number Below", font="roboto 12", bg="White", fg="Black")
        self.sub.place(relx="0.2", rely="0.5")

        self.ID = Entry(self.frame, width="35", fg="#007f5f")
        self.ID.place(relx="0.14", rely="0.61")

        self.IDl = Label(self.frame, text="ID Number", font="Google-Sans 10", bg="white", fg="#007f5f")
        self.IDl.place(relx="0.16", rely="0.57")

        self.login = Button(self.frame, text="Login", font="Google-Sans 10", bg="white", fg="#007f5f", width="12",
                            borderwidth="0",
                            activebackground='#55a630', highlightbackground="#007f5f",
                            activeforeground="#ffffff", command=
                            self.opt1)
        self.login.place(relx="0.14", rely="0.7")

        self.signupb = Button(self.frame, text="Sign up?", font="Google-Sans 10", bg="white", fg="#007f5f", width="12",
                              borderwidth="0",
                              activebackground='#55a630', highlightbackground="#007f5f",
                              activeforeground="#ffffff", command=self.opt2)
        self.signupb.place(relx="0.55", rely="0.7")

        self.exit = Button(self.frame, text="Exit", font="Google-Sans 9", bg="white", fg="#007f5f", width="33",
                           borderwidth="0",
                           activebackground='#55a630', highlightbackground="#007f5f",
                           activeforeground="#ffffff", command=self.exit)
        self.exit.place(relx="0.13", rely="0.82")

        self.master.mainloop()

    def exit(self):
        res = messagebox.askyesno("Warning", "You are about to exit the program, Continue?")
        if res:
            root.destroy()

    def admin(self, event=None):
        root.withdraw()
        import admin

    def opt2(self):
        root.withdraw()
        import window

    def opt1(self):
        ID = self.ID.get()

        mycursor.execute("select * from Users where ID='{}'".format(ID))
        result = mycursor.fetchall()
        if ID == "":
            messagebox.showerror("Error", "Please enter information")
        elif result:
            messagebox.showinfo("Welcome", "Welcome Back!")
            root.withdraw()
            import signout
        else:
            messagebox.showerror("Error", "Please Enter Valid Information")


Login(root)
