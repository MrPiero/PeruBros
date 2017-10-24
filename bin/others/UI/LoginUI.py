from tkinter import *


class LoginUIMenu:
    def __init__(self, root):
        frame = Frame(root)
        frame.pack()

        self.labelUser = Label(frame, text="Username:")
        self.labelPasswd = Label(frame, text="Password:")

        self.labelUser.grid(row=0, sticky=E)
        self.labelPasswd.grid(row=1, sticky=E)

        self.entryUser = Entry(frame)
        self.entryPasswd = Entry(frame, show="*")

        self.entryUser.grid(row=0, column=1)
        self.entryPasswd.grid(row=1, column=1)

        self.buttonSubmit = Button(frame, text="Submit", command=self.login)
        self.buttonSubmit.grid(columnspan=2)

    def login(self):
        print(self.entryPasswd.get())
