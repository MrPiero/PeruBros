import unittest
from bin.others.UI.LoginUI import LoginUIMenu
from bin.game import main as game
from bin.others.levelReader import uncode as lv_read

class TestBasico(unittest.TestCase):

    def test_login_incorrecto(self):
        login = LoginUIMenu()
        login.comprobar_user("unittest", "unittest")
        self.assertEqual(False, login.status)

    def test_login_correcto(self):
        login = LoginUIMenu()
        login.comprobar_user("Piero Bardelli", "unittest123")
        self.assertEqual(True, login.status)

    def test_muerte_PorEnemigo(self):
        g = game((1, 1))
        self.assertEqual(1,g[1]['death_type'])

    def test_muerte_PorCaida(self):
        g = game((1, 1))
        self.assertEqual(2,g[1]['death_type'])

    def test_desarrollo_de_niveles(self):
        a = lv_read('lvl_x_x')
        self.assertEqual([[[(70, 0, 70, 70), 50, 550], [(70, 0, 70, 70), -20, 550], [(70, 0, 70, 70), 50, 480], [(70, 0, 70, 70), -20, 480], [(70, 0, 70, 70), 50, 410], [(70, 0, 70, 70), -20, 410], [(70, 0, 70, 70), 50, 340], [(70, 0, 70, 70), -20, 340], [(70, 0, 70, 70), 50, 270], [(70, 0, 70, 70), -20, 270], [(70, 0, 70, 70), 50, 200], [(70, 0, 70, 70), -20, 200], [(70, 0, 70, 70), 50, 130], [(70, 0, 70, 70), -20, 130], [(70, 0, 70, 70), 50, 60], [(70, 0, 70, 70), -20, 60], [(70, 0, 70, 70), 50, -10], [(70, 0, 70, 70), -20, -10], [(70, 0, 70, 70), 50, -80], [(70, 0, 70, 70), -20, -80], [(0, 0, 70, 70), 500, 490], [(70, 140, 70, 70), 120, 550], [(70, 140, 70, 70), 190, 550], [(70, 0, 70, 70), 330, 340]], [], [], 500] ,a)

