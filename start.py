import sys
from bin.others.UI.LoginUI import LoginUIMenu
from bin.others.UI.GameMenuUI import GameUIMenu
from bin.others.UI.LevelMenuUI import LevelUIMenu
from bin.game import main as game
from bin.test_main import test as t
import bin.others.Data.DAO as DAO
import bin.constants

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
            print("valor: " + str(val[0]))
            print(LevelMenu.save['id_personaje'])
            DAO.save_score(LevelMenu.save['id_personaje'],val[1]['score'])
            if (val[1]['death_type'] == 0):
                DAO.save_progress(LevelMenu.save['id_personaje'], bin.constants.nxt_lv[progress])

    else:
        print("LOGIN CERRADO.")
elif sys.argv[1] == 'test1':
    LevelMenu = LevelUIMenu()
    LevelMenu.main_menu()
elif sys.argv[1] == 'test2':
    g = game((3,3))
    print(g[1])
elif sys.argv[1] == 'test3':
    t()
elif sys.argv[1] == 'test4':
    DAO.save_progress(2, (1, 2))
    # DAO.save_score(2, 5000)
