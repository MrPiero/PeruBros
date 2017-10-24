# Este archivo esta encargado de inicializar la aplicacion

# from bin import main
import sys, tkinter
from bin.others.UI.LoginUI import LoginUIMenu

if len(sys.argv) == 1:
    # main.main()
    # root = Tk()
    LoginUIMenu()
    # root.mainloop()


elif sys.argv[1] == 'test':
    pass