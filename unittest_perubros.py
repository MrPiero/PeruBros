import unittest
from bin.others.UI.LoginUI import LoginUIMenu


class TestLogin(unittest.TestCase):

    def test_login_incorrecto(self):
        login = LoginUIMenu()
        login.comprobar_user("unittest", "unittest")
        self.assertEqual(False, login.status)

    def test_login_correcto(self):
        login = LoginUIMenu()
        login.comprobar_user("Piero Bardelli", "unittest123")
        self.assertEqual(True, login.status)
