import unittest
from bin.others.UI.LoginUI import LoginUIMenu
from bin.game import main as game

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
        self.assertEqual(0,g[0])

