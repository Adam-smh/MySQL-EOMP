from tkinter import *
from tkinter import ttk
import mysql.connector

root = Tk()
root.title('Admin Control')
root.geometry('2000x1000')


class Screen:
    def __init__(self, master):

        self.frame = Frame(master, border="1", width=700, height=600, relief="groove", borderwidth=1, bg="#ffffff")
        self.frame.place(relx="0.23", rely="0.1")

        self.title = Label(self.frame, text="Users", font="Sans-Serif 18", bg="white")
        self.title.place(relx="0.44", rely="0.05")

        self.tree = ttk.Treeview(self.frame)

        self.tree['columns'] = ('Name', 'ID', 'Phone')
        self.tree.column('#0', width=0, stretch=NO)
        self.tree.column('Name', anchor=CENTER, width=200)
        self.tree.column('ID', anchor=CENTER, width=200)
        self.tree.column('Phone', anchor=CENTER, width=200)

        self.tree['show'] = 'headings'
        self.tree.heading('Name', text='Name')
        self.tree.heading('ID', text='ID')
        self.tree.heading('Phone', text='Phone')

        self.users()

        self.tree.place(rely="0.15", relx="0.058")

        self.add = Button(self.frame, text="Add/Remove", font="Google-Sans 10", bg="white", fg="#007f5f", width="12",
                          borderwidth="0",
                          activebackground='#55a630', highlightbackground="#007f5f",
                          activeforeground="#ffffff", command=self.add)
        self.add.place(relx="0.12", rely="0.55")

        self.editb = Button(self.frame, text="Edit", font="Google-Sans 10", bg="white", fg="#007f5f", width="12",
                          borderwidth="0",
                          activebackground='#55a630', highlightbackground="#007f5f",
                          activeforeground="#ffffff")
        self.editb.place(relx="0.4", rely="0.55")

        self.adminb = Button(self.frame, text="Add Admin", font="Google-Sans 10", bg="white", fg="#007f5f", width="12",
                          borderwidth="0",
                          activebackground='#55a630', highlightbackground="#007f5f",
                          activeforeground="#ffffff", command=self.addadmin)
        self.adminb.place(relx="0.68", rely="0.55")

    def users(self):
        mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                       database='LifechoicesOnline',
                                       auth_plugin='mysql_native_password')
        mycursor = mydb.cursor()
        info = "select * from Users"
        mycursor.execute(info)
        data = mycursor.fetchall()

        self.tree.delete(*self.tree.get_children())
        for user in data:
            self.tree.insert(parent="", index="end", text="", values=user)

    def add(self):
        root.withdraw()
        import add

    def edit(self):
        root.destroy()
        import deledit

    def addadmin(self):
        root.withdraw()
        import addadmin


Screen(root)
root.mainloop()
