import datetime
from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage
import mysql.connector

x = datetime.datetime.now()
print(x)

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

        self.frame = Frame(self.master, border="1", width=400, height=400, relief="groove", borderwidth=1, bg="#ffffff")
        self.frame.place(relx="0.35", rely="0.2")

        logo = PhotoImage(file="/home/adam/Documents/Python/lc.png", master=self.master)
        logo = logo.subsample(2)
        self.lg = Label(self.frame, image=logo, bg="#007f5f", width="400", height="150")
        self.lg.place(relx="-0.01", rely="-0.01")

        self.signin = Label(self.frame, text="Welcome", font="Google-Sans 18", bg="White", fg="Black")
        self.signin.place(relx="0.38", rely="0.4")

        self.sub = Label(self.frame, text="Sign out when youre ready", font="roboto 12", bg="White", fg="Black")
        self.sub.place(relx="0.2", rely="0.5")

        self.exit = Button(self.frame, text="Sign Out", font="Google-Sans 9", bg="white", fg="#007f5f", width="33",
                           borderwidth="0",
                           activebackground='#55a630', highlightbackground="#007f5f",
                           activeforeground="#ffffff", command=self.out)
        self.exit.place(relx="0.13", rely="0.82")

        self.master.mainloop()

    def out(self):
        res = messagebox.askyesno("Warning", "You are about to exit the program, Continue?")
        if res:
            root.destroy()


Login(root)
