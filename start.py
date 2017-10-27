# Este archivo esta encargado de inicializar la aplicacion

import sys
from bin.others.UI.LoginUI import LoginUIMenu
from bin.others.UI.GameMenuUI import GameUIMenu
from bin.test_game import main as test_game

if len(sys.argv) == 1:
    login = LoginUIMenu()
    idUser = login.main()
    if login.status:
        print("ABRIENDO EL JUEGO...")
        GameMenu = GameUIMenu(idUser)
        GameMenu.main_menu()
        # SEA LA PARTIDA QUE SE HAYA SELECCIONADO
        # POR AHORA SE CARGA EL TEST DEL JUEGO
        #
        # NOTA IMPORTATE:
        # POR SER UN TEST, SE DEMORA UN POCO EN CARGAR EL JUEGO, PERO SÍ FUNCIONA.
        # EL FUNCIONAMIENTO EN WINDOWS ES NORMAL, EN MAC TIENE BAJONES DE FPS.
        # EL PERSONAJE AÚN NO MUERE POR CAÍDAS.
        test_game()
        print("TEST")
    else:
        print("LOGIN CERRADO.")
elif sys.argv[1] == 'test':
    test_game()
