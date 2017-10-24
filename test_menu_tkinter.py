from tkinter import *

root = Tk()  # Ventana
""" # the_label = Label(root, text="This is too easy")  # Texto del label
# the_label.pack()  # Lo pone en la ventana

top_frame = Frame(root)
top_frame.pack()
bottom_frame = Frame(root)
bottom_frame.pack(side=BOTTOM)

button1 = Button(top_frame, text="Button 1", fg="red")
button2 = Button(top_frame, text="Button 2", fg="blue")
button3 = Button(top_frame, text="Button 3", fg="green")
button4 = Button(bottom_frame, text="Button 4", fg="purple")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)

one = Label(root, text="One", bg="red", fg="white")
one.pack()
two = Label(root, text="Two", bg="green", fg="black")
two.pack(fill=X)  # Que el texto crezca de acuerdo al axis X de root
three = Label(root, text="Three", bg="blue", fg="white")
three.pack(side=LEFT, fill=Y)"""


"""

# PASSWORD - LOGIN

def show():  # Add "event" as param to bind
    print(passwd.get())


label_1 = Label(root, text="Name")
label_2 = Label(root, text="Password")
entry_1 = Entry(root)
passwd = StringVar()
entry_2 = Entry(root, show="*", textvariable=passwd)

label_1.grid(row=0, sticky=E)
label_2.grid(row=1, sticky=E)

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

c = Checkbutton(root, text="Keep me logged in")
c.grid(columnspan=2)

button = Button(root, text="Submit", command=show)
# button.bind("<Button-1>", show)
button.grid(columnspan=2)

"""

"""

# MOUSE EVENTS

def leftClick(event):
    print("Left")


def rightClick(event):
    print("Right")


frame = Frame(root, width=300, height=250)
frame.bind("<Button-1>", leftClick)
frame.bind("<Button-3>", rightClick)
frame.pack()

"""

# USING CLASSES

class BuckysButton:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame, text="Print Message", command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text="Quit", command=frame.quit)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print("TEST")


b = BuckysButton(root)
root.mainloop()
