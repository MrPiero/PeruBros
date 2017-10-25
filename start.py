# Este archivo esta encargado de inicializar la aplicacion

# from bin import main
import sys, tkinter
from bin.others.UI.LoginUI import LoginUIMenu

if len(sys.argv) == 1:
    login = LoginUIMenu()
    login.main()
    if login.status:
        print("ABRIENDO EL JUEGO...")
    else:
        print("LOGIN CERRADO.")

elif sys.argv[1] == 'test':
    pass