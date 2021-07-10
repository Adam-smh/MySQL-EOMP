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


class Edit:
    def __init__(self, master):
        self.master = master
        self.master.title("Life Choices")
        self.master.geometry("2000x1000")

        self.frame = Frame(self.master, border="1", width=400, height=400, relief="groove", borderwidth=1, bg="#ffffff")
        self.frame.place(relx="0.35", rely="0.23")

        self.sub = Label(self.frame, text="Enter ID number of user", font="roboto 12", bg="White", fg="Black")
        self.sub.place(relx="0.26", rely="0.2")

        self.ID = Entry(self.frame, width="35", fg="#007f5f")
        self.ID.place(relx="0.14", rely="0.5")

        self.IDl = Label(self.frame, text="ID Number", font="Google-Sans 10", bg="white", fg="#007f5f")
        self.IDl.place(relx="0.16", rely="0.47")

        self.editb = Button(self.frame, text="Edit", font="Google-Sans 10", bg="white", fg="#007f5f", width="12",
                           borderwidth="0",
                           activebackground='#55a630', highlightbackground="#007f5f",
                           activeforeground="#ffffff", command=self.edit)
        self.editb.place(relx="0.14", rely="0.7")

        self.cancelb = Button(self.frame, text="Cancel", font="Google-Sans 10", bg="white", fg="#007f5f", width="12",
                           borderwidth="0",
                           activebackground='#55a630', highlightbackground="#007f5f",
                           activeforeground="#ffffff", command=self.cancel)
        self.cancelb.place(relx="0.55", rely="0.7")

        self.master.mainloop()

    def edit(self):

        ID = self.ID.get()

        mycursor.execute("select * from Users where ID='{}'".format(ID))
        result1 = mycursor.fetchall()

        if ID == "":
            messagebox.showerror("Error", "Please fill all fields")

        elif len(ID) != 13:
            messagebox.showerror("Error", "Please enter correct ID number")

        else:

            log_3 = "delete from Users where ID='{}'" .format(ID)
            mycursor.execute(log_3)
            mydb.commit()

            root.withdraw()
            import edit

    def cancel(self):

            root.withdraw()
            import prac


Edit(root)
