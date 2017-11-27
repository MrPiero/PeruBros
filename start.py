import sys
from bin.others.UI.LoginUI import LoginUIMenu
from bin.others.UI.GameMenuUI import GameUIMenu
from bin.others.UI.LevelMenuUI import LevelUIMenu
from bin.game import main as game
from bin.test_main import test as t
import bin.others.Data.DAO as DAO

if len(sys.argv) == 1:
    login = LoginUIMenu()
    idUser = login.main()
    print(login.status)
    if login.status:
        GameMenu = GameUIMenu(idUser)
        save = GameMenu.main_menu()
        val = [1,0]
        while val[0] == 1:
            # Val = 1 : El usuario gano el nivel
            # Val = 0 : El usuario fallo el nivel
            LevelMenu = LevelUIMenu(save)
            progress = LevelMenu.main_menu()
            print(progress)
            val = game(progress)
            stats = val[1]
            print(val[1])

    else:
        print("LOGIN CERRADO.")
elif sys.argv[1] == 'test1':
    LevelMenu = LevelUIMenu()
    LevelMenu.main_menu()
elif sys.argv[1] == 'test2':
    g = game((3,2))
    print(g[1])
elif sys.argv[1] == 'test3':
    t()
elif sys.argv[1] == 'test4':
    DAO.save_progress(2, (1, 2))
