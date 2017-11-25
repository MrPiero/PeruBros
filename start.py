import sys
from bin.others.UI.LoginUI import LoginUIMenu
from bin.others.UI.GameMenuUI import GameUIMenu
from bin.others.UI.LevelMenuUI import LevelUIMenu
# from bin.test_game import main as test_game
from bin.game import main as game
from bin.test_main import test as t

if len(sys.argv) == 1:
    login = LoginUIMenu()
    idUser = login.main()
    print(login.status)
    if login.status:
        GameMenu = GameUIMenu(idUser)
        save = GameMenu.main_menu()
        val = 1
        while val == 1:
            LevelMenu = LevelUIMenu(save)
            progress = LevelMenu.main_menu()
            print(progress)
            if progress == (1, 1):
                # test_game()
                val = game()
            else:
                print("Nivel ", progress, " seleccionado")

    else:
        print("LOGIN CERRADO.")
elif sys.argv[1] == 'test1':
    LevelMenu = LevelUIMenu()
    LevelMenu.main_menu()
elif sys.argv[1] == 'test2':
    # test_game()
    game()
elif sys.argv[1] == 'test3':
    t()
