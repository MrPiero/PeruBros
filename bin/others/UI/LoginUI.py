from tkinter import *
import json
import requests


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

        # self.root.mainloop()
        self.status = False
        self.idUser = 0

    def main(self):
        logo = PhotoImage(file="resources/logos/perubrologo.png")
        self.labelLogo = Label(self.frameLogo, image=logo)
        self.labelLogo.pack()  # grid(columnspan=2)
        self.root.mainloop()
        return self.idUser

    def login_file(self):
        # LOGIN DESDE UN ARCHIVO JSON
        u = self.entryUser.get()
        p = self.entryPasswd.get()

        json_file = open("test_json.txt", "r")
        user = json.load(json_file)
        json_file.close()

        if user["username"] == u and user["password"] == p:
            self.root.quit()
        else:
            print("CREDENCIALES INCORRECTAS")

    def login_https(self):
        # LOGIN DESDE UN STRING JSON DESDE HTTPS
        u = self.entryUser.get()
        p = self.entryPasswd.get()
        url = "https://jsonplaceholder.typicode.com/users"
        json_file = requests.get(url).json()

        for user in json_file:
            if user["name"] == u and user["username"] == p:
                # DEL LINK DE MUESTRA SE OBTIENEN ESTOS EJEMPLOS
                #
                # name : Leanne Graham
                # username : Bret
                #
                # name : Ervin Howell
                # username : Antonette
                print(user)
                self.root.quit()
                self.status = True
                self.idUser = user["id"]
        if not self.status: print("CREDENCIALES INCORRECTAS")

