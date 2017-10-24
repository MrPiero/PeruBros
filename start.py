# Este archivo esta encargado de inicializar la aplicacion

# from bin import main
import sys, tkinter
from bin.others.UI.LoginUI import LoginUIMenu

if len(sys.argv) == 1:
    # main.main()
    # root = Tk()
    login = LoginUIMenu()
    # root.mainloop()
    status = login.main()
    print(status)

elif sys.argv[1] == 'test':
    pass