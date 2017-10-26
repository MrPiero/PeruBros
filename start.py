# Este archivo esta encargado de inicializar la aplicacion

# from bin import main
import sys
from bin.others.UI.LoginUI import LoginUIMenu
# from bin.main_test import main
from bin.others.UI.GameMenuUI import GameUIMenu

if len(sys.argv) == 1:
    login = LoginUIMenu()
    idUser = login.main()
    if login.status:
        print("ABRIENDO EL JUEGO...")
        GameMenu = GameUIMenu(idUser)
        GameMenu.main_menu()
        print("TEST")
    else:
        print("LOGIN CERRADO.")

elif sys.argv[1] == 'test':
    pass