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
root.geometry("1000x1000")
root.config(bg="#55a630")


class Login:
    def __init__(self, master):
        self.master = master
        self.master.title("Life Choices")
        self.master.geometry("2000x1000")

        self.master.bind('<Control-a>', self.admin)

        self.frame = Frame(self.master, border="1", width=400, height=700, relief="groove", borderwidth=1, bg="#ffffff")
        self.frame.place(relx="0.35", rely="0.0")

        logo = PhotoImage(file="/home/adam/Documents/Python/lc.png", master=self.master)
        logo = logo.subsample(2)
        self.lg = Label(self.frame, image=logo, bg="#007f5f", width="400", height="150")
        self.lg.place(relx="-0.01", rely="-0.01")

        self.signupl = Label(self.frame, text="Sign up", font="Google-Sans 18", bg="White", fg="Black")
        self.signupl.place(relx="0.38", rely="0.22")

        self.sub = Label(self.frame, text="Enter your details below", font="roboto 12", bg="White", fg="Black")
        self.sub.place(relx="0.24", rely="0.3")

        self.name = Entry(self.frame, width="35", fg="#007f5f")
        self.name.place(relx="0.14", rely="0.39")

        self.namel = Label(self.frame, text="Username", font="Google-Sans 10", bg="white", fg="#007f5f")
        self.namel.place(relx="0.16", rely="0.37")

        self.phone = Entry(self.frame, width="35", fg="#007f5f")
        self.phone.place(relx="0.14", rely="0.46")

        self.phonel = Label(self.frame, text="Phone", font="Google-Sans 10", bg="white", fg="#007f5f")
        self.phonel.place(relx="0.16", rely="0.44")

        self.ID = Entry(self.frame, width="35", fg="#007f5f")
        self.ID.place(relx="0.14", rely="0.52")

        self.IDl = Label(self.frame, text="ID Number", font="Google-Sans 10", bg="white", fg="#007f5f")
        self.IDl.place(relx="0.16", rely="0.5")

        self.KNamel = Label(self.frame, text="Next of Kin Name", font="Google-Sans 10", bg="white", fg="#007f5f")
        self.KNamel.place(relx="0.16", rely="0.57")

        self.KName = Entry(self.frame, width="35", fg="#007f5f")
        self.KName.place(relx="0.14", rely="0.59")

        self.KPhone = Entry(self.frame, width="35", fg="#007f5f")
        self.KPhone.place(relx="0.14", rely="0.65")

        self.KPhonel = Label(self.frame, text="Next of Kin Phone", font="Google-Sans 10", bg="white", fg="#007f5f")
        self.KPhonel.place(relx="0.16", rely="0.63")

        self.signup = Button(self.frame, text="Sign up", font="Google-Sans 10", bg="white", fg="#007f5f", width="12",
                             borderwidth="0",
                             activebackground='#55a630', highlightbackground="#007f5f",
                             activeforeground="#ffffff", command=self.Signup)
        self.signup.place(relx="0.14", rely="0.8")

        self.login = Button(self.frame, text="Login?", font="Google-Sans 10", bg="white", fg="#007f5f", width="12",
                            borderwidth="0",
                            activebackground='#55a630', highlightbackground="#007f5f",
                            activeforeground="#ffffff", command=self.Login)
        self.login.place(relx="0.55", rely="0.8")

        self.exit = Button(self.frame, text="Exit", font="Google-Sans 9", bg="white", fg="#007f5f", width="33",
                           borderwidth="0",
                           activebackground='#55a630', highlightbackground="#007f5f",
                           activeforeground="#ffffff", command=self.exit)
        self.exit.place(relx="0.13", rely="0.9")

        self.master.mainloop()

    def exit(self):
        res = messagebox.askyesno("Warning", "You are about to exit the program, Continue?")
        if res:
            root.destroy()

    def admin(self, event=None):
        root.withdraw()
        import admin

    def Login(self):
        root.withdraw()
        import main

    def Signup(self):
        N = self.name.get()
        P = self.phone.get()
        ID = self.ID.get()
        kn = self.KName.get()
        kp = self.KPhone.get()

        mycursor.execute("select * from Users where Phone='{}'".format(P))
        result2 = mycursor.fetchall()
        mycursor.execute("select * from Users where ID='{}'".format(ID))
        result3 = mycursor.fetchall()

        if N == "" or P == "" or ID == "":
            messagebox.showerror("Error", "Please fill all fields")

        elif result2 or result3:
            messagebox.showerror("Error", "User details already exists, please Login.")

        elif len(P) != 10:
            messagebox.showerror("Error", "Please enter correct number")

        elif len(ID) != 13:
            messagebox.showerror("Error", "Please enter correct ID number")

        else:
            messagebox.showinfo("Welcome!", N)

            log_1 = "insert into Users (Name, ID, Phone) values ('{}', '{}', '{}')".format(N, ID, P)
            log_2 = "insert into Nextofkin (Name, Phone, User_ID) values ('{}', '{}', '{}')".format(kn, kp, ID)
            mycursor.execute(log_1)
            mycursor.execute(log_2)
            mydb.commit()
            root.withdraw()
            import signout


Login(root)
