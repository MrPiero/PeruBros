from tkinter import *
import requests
import bin.constants as GC
import bcrypt


class LoginUIMenu:
    def __init__(self):
        self.root = Tk()
        self.root.title("PERUBROS.")
        self.root.geometry("1280x500")

        self.frameLogo = Frame(self.root)
        self.frameLogo.pack()
        frame = Frame(self.root, width=300)
        frame.pack()

        self.labelUser = Label(frame, text="Username:")
        self.labelPasswd = Label(frame, text="Password:")

        self.labelUser.grid(row=2, sticky=E)
        self.labelPasswd.grid(row=3, sticky=E)

        self.entryUser = Entry(frame)
        self.entryPasswd = Entry(frame, show="*")

        self.entryUser.grid(row=2, column=1, sticky=W)
        self.entryPasswd.grid(row=3, column=1, sticky=W)

        self.buttonSubmit = Button(frame, text="Log In", command=self.login_https)
        self.buttonSubmit.grid(columnspan=2)

        self.status = False
        self.idUser = 0

    def main(self):
        logo = PhotoImage(file=GC.LOGO_PATH)
        self.labelLogo = Label(self.frameLogo, image=logo)
        self.labelLogo.pack()  # grid(columnspan=2)
        self.root.mainloop()
        return self.idUser

    def login_https(self):
        # LOGIN DESDE UN STRING JSON DESDE HTTPS
        u = self.entryUser.get()
        p = self.entryPasswd.get().encode("utf-8")
        # p = bcrypt.hashpw(p, bcrypt.gensalt())
        json_file = requests.get(GC.URL).json()
        for user in json_file:
            print(user["name"], user["password"].encode("utf-8"))
            print(u, p)
            # print(bcrypt.checkpw(p, user["password"]))
            if user["name"] == u:

                self.root.quit()
                self.status = True
                self.idUser = user["id"]
            if u == "test" and p == "test":
                self.root.quit()
                self.status = True
                self.idUser = 1
        if not self.status:
            print("CREDENCIALES INCORRECTAS")
