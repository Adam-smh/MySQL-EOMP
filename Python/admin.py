from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage
import mysql.connector

root = Tk()
root.title("Login")
root.geometry("1000x1000")
root.config(bg="#55a630")

mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                               database='LifechoicesOnline',
                               auth_plugin='mysql_native_password')
mycursor = mydb.cursor()


class Login:
    def __init__(self, master):
        self.master = master
        self.master.title("Life Choices")
        self.master.geometry("2000x1000")

        self.frame = Frame(self.master, border="1", width=400, height=400, relief="groove", borderwidth=1, bg="#ffffff")
        self.frame.place(relx="0.35", rely="0.2")

        logo = PhotoImage(file="/home/adam/Documents/Python/lc.png", master=self.master)
        logo = logo.subsample(2)
        self.lg = Label(self.frame, image=logo, bg="#007f5f", width="400", height="150")
        self.lg.place(relx="-0.01", rely="-0.01")

        self.signin = Label(self.frame, text="Admin Sign in", font="Google-Sans 18", bg="White", fg="Black")
        self.signin.place(relx="0.28", rely="0.4")

        self.sub = Label(self.frame, text="Enter Your Details Below", font="roboto 12", bg="White", fg="Black")
        self.sub.place(relx="0.25", rely="0.5")

        self.ID = Entry(self.frame, width="35", fg="#007f5f")
        self.ID.place(relx="0.14", rely="0.61")

        self.IDl = Label(self.frame, text="ID Number", font="Google-Sans 10", bg="white", fg="#007f5f")
        self.IDl.place(relx="0.16", rely="0.57")

        self.Pass = Entry(self.frame, width="35", fg="#007f5f")
        self.Pass.place(relx="0.14", rely="0.71")

        self.Passl = Label(self.frame, text="Password", font="Google-Sans 10", bg="white", fg="#007f5f")
        self.Passl.place(relx="0.16", rely="0.67")

        self.login = Button(self.frame, text="Login", font="Google-Sans 10", bg="white", fg="#007f5f", width="12",
                            borderwidth="0",
                            activebackground='#55a630', highlightbackground="#007f5f",
                            activeforeground="#ffffff", command=
                            self.login)
        self.login.place(relx="0.35", rely="0.8")

        self.exit = Button(self.frame, text="Exit", font="Google-Sans 9", bg="white", fg="#007f5f", width="12",
                           borderwidth="0",
                           activebackground='#55a630', highlightbackground="#007f5f",
                           activeforeground="#ffffff", command=self.exit)
        self.exit.place(relx="0.35", rely="0.9")

        self.master.mainloop()

    def exit(self):
        res = messagebox.askyesno("Warning", "You are about to exit the program, Continue?")
        if res:
            root.destroy()

    def login(self):

        ID = self.ID.get()
        P = self.Pass.get()

        mycursor.execute("select * from Admin where Pass='{}'".format(P))
        result1 = mycursor.fetchall()
        mycursor.execute("select * from Admin where ID='{}'".format(ID))
        result2 = mycursor.fetchall()

        if len(ID) != 13:
            messagebox.showerror("Error", "Invalid ID Entry")

        elif result1 and result2:
            root.destroy()
            import prac

        elif not result1:
            messagebox.showerror("Error","Incorrect Password")

        elif not result2:
            messagebox.showerror("Error","Incorrect ID Number")


Login(root)
