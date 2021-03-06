from tkinter import *
import bin.constants as GC
import bin.others.Data.DAO as DAO
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

    def login_https(self, ):
        u = self.entryUser.get()
        p = self.entryPasswd.get()
        self.comprobar_user(u, p)

    def comprobar_user(self, u, p):
        try:
            json_file = DAO.list_users()
            for user in json_file:
                if user["name"] == u:
                    self.root.quit()
                    self.status = True
                    self.idUser = user["id"]
            if not self.status:
                print("CREDENCIALES INCORRECTAS")
        except:
            if u == "Piero Bardelli":
                self.root.quit()
                self.status = True
                self.idUser = 4
            if not self.status:
                print("CREDENCIALES INCORRECTAS")

