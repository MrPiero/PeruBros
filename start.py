# Este archivo esta encargado de inicializar la aplicacion

# from bin import main
import sys
from bin.others.UI.LoginUI import LoginUIMenu
# from bin.main_test import main
from bin.others.UI.GameMenuUI import main

if len(sys.argv) == 1:
    login = LoginUIMenu()
    login.main()
    if login.status:
        print("ABRIENDO EL JUEGO...")
        main()
    else:
        print("LOGIN CERRADO.")

elif sys.argv[1] == 'test':
    pass