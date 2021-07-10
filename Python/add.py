from tkinter import *
from tkinter import messagebox
import mysql.connector

root = Tk()
root.title('Admin Control')
root.geometry('700x500')
root.config(bg="#55a630")

mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                               database='LifechoicesOnline',
                               auth_plugin='mysql_native_password')
mycursor = mydb.cursor()


class Add:
    def __init__(self, master):
        self.master = master
        self.master.title("Life Choices")
        self.master.geometry("2000x1000")

        self.frame = Frame(self.master, border="1", width=400, height=550, relief="groove", borderwidth=1, bg="#ffffff")
        self.frame.place(relx="0.35", rely="0.1")

        self.sub = Label(self.frame, text="Enter details below", font="roboto 12", bg="White", fg="Black")
        self.sub.place(relx="0.3", rely="0.2")

        self.name = Entry(self.frame, width="35", fg="#007f5f")
        self.name.place(relx="0.14", rely="0.4")

        self.namel = Label(self.frame, text="Username", font="Google-Sans 10", bg="white", fg="#007f5f")
        self.namel.place(relx="0.16", rely="0.37")

        self.phone = Entry(self.frame, width="35", fg="#007f5f")
        self.phone.place(relx="0.14", rely="0.5")

        self.phonel = Label(self.frame, text="Phone", font="Google-Sans 10", bg="white", fg="#007f5f")
        self.phonel.place(relx="0.16", rely="0.47")

        self.ID = Entry(self.frame, width="35", fg="#007f5f")
        self.ID.place(relx="0.14", rely="0.6")

        self.IDl = Label(self.frame, text="ID Number", font="Google-Sans 10", bg="white", fg="#007f5f")
        self.IDl.place(relx="0.16", rely="0.57")

        self.addb = Button(self.frame, text="Add", font="Google-Sans 10", bg="white", fg="#007f5f", width="12",
                           borderwidth="0",
                           activebackground='#55a630', highlightbackground="#007f5f",
                           activeforeground="#ffffff", command=self.addf)
        self.addb.place(relx="0.14", rely="0.7")

        self.remb = Button(self.frame, text="Remove", font="Google-Sans 10", bg="white", fg="#007f5f", width="12",
                           borderwidth="0",
                           activebackground='#55a630', highlightbackground="#007f5f",
                           activeforeground="#ffffff", command=self.remove)
        self.remb.place(relx="0.55", rely="0.7")

        self.master.mainloop()

    def addf(self):
        N = self.name.get()
        P = self.phone.get()
        ID = self.ID.get()

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
            messagebox.showinfo("Added", N)

            log_1 = "insert into Users (Name, ID, Phone) values ('{}', '{}', '{}')".format(N, ID, P)

            mycursor.execute(log_1)
            mydb.commit()
            root.destroy()
            import prac

    def remove(self):

        N = self.name.get()
        P = self.phone.get()
        ID = self.ID.get()

        mycursor.execute("select * from Users where Name='{}'".format(N))
        result1 = mycursor.fetchall()
        mycursor.execute("select * from Users where Phone='{}'".format(P))
        result2 = mycursor.fetchall()
        mycursor.execute("select * from Users where ID='{}'".format(ID))
        result3 = mycursor.fetchall()

        if N == "" or P == "" or ID == "":
            messagebox.showerror("Error", "Please fill all fields")

        elif len(P) != 10:
            messagebox.showerror("Error", "Please enter correct number")

        elif len(ID) != 13:
            messagebox.showerror("Error", "Please enter correct ID number")

        elif result1 and result2 and result3:
            messagebox.showinfo("removed", N)

            log_2 = "delete from Users where ID='{}'".format(ID)

            mycursor.execute(log_2)
            mydb.commit()
            root.withdraw()
            import prac


Add(root)
