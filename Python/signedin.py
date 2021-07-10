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

        self.frame = Frame(self.master, border="1", width=900, height=600, relief="groove", borderwidth=1, bg="#ffffff")
        self.frame.place(relx="0.15", rely="0.07")

        self.sub1 = Label(self.frame, text="Name", font="Google-Sans", bg="White", fg="Black")
        self.sub1.place(relx="0.1", rely="0.1")

        # self.sub2
        # self.sub2
        #
        # self.sub3
        # self.sub3
        #
        # self.sub4
        # self.sub4



        self.master.mainloop()