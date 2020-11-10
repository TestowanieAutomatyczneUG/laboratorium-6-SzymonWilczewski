import unittest

from src.zad02.main import Password


class PasswordTest(unittest.TestCase):
    def setUp(self):
        self.password = Password()

    def test_valid_password_1(self):
        self.assertTrue(self.password.ValidPassword("ABCDEF123456!?"))

    def test_valid_password_2(self):
        self.assertTrue(self.password.ValidPassword("123!!!123ABC"))

    def test_valid_password_3(self):
        self.assertTrue(self.password.ValidPassword("Password$123"))

    def test_password_without_capital_letter(self):
        self.assertFalse(self.password.ValidPassword("abcdef123456!?"))

    def test_password_without_sign(self):
        self.assertFalse(self.password.ValidPassword("123123ABC"))

    def test_password_without_number(self):
        self.assertFalse(self.password.ValidPassword("PASSWORD!!!"))

    def test_password_with_signs_only(self):
        self.assertFalse(self.password.ValidPassword("!!!!!!!!"))

    def test_too_short_password(self):
        self.assertFalse(self.password.ValidPassword("A1!"))

    def test_wrong_type(self):
        with self.assertRaises(TypeError):
            self.password.ValidPassword(True)

    def test_password_with_space(self):
        with self.assertRaises(ValueError):
            self.password.ValidPassword("Pass word 123 !!!")

    def tearDown(self):
        self.password = None
