import unittest
import bin.others.UI.LevelMenuUI as LoginUIMenu


class TestLogin(unittest.TestCase):

    def test_login_incorrecto(self):
        login = LoginUIMenu
        print(login)
        self.assertEqual(False, login.status)
