import re


class Password:
    def ValidPassword(self, password):
        """
        >>> password = Password()
        >>> password.ValidPassword("ABCDEF123456!?")
        True
        >>> password.ValidPassword("123!!!123ABC")
        True
        >>> password.ValidPassword("Password$123")
        True
        >>> password.ValidPassword("abcdef123456!?")
        False
        >>> password.ValidPassword("123123ABC")
        False
        >>> password.ValidPassword("PASSWORD!!!")
        False
        >>> password.ValidPassword("!!!!!!!!")
        False
        >>> password.ValidPassword("A1!")
        False
        >>> password.ValidPassword(True)
        Traceback (most recent call last):
          File "C:/Users/Szymon/PycharmProjects/Testowanie Automatyczne/laboratorium-6-SzymonWilczewski/src/zad02/main.py", line 35, in <module>
            print(Password.ValidPassword(Password, True))
          File "C:/Users/Szymon/PycharmProjects/Testowanie Automatyczne/laboratorium-6-SzymonWilczewski/src/zad02/main.py", line 25, in ValidPassword
            if ' ' in password:
        TypeError: argument of type 'bool' is not iterable
        >>> password.ValidPassword("Pass word 123 !!!")
        Traceback (most recent call last):
          File "C:/Users/Szymon/PycharmProjects/Testowanie Automatyczne/laboratorium-6-SzymonWilczewski/src/zad02/main.py", line 43, in <module>
            print(Password.ValidPassword(Password, "Pass word 123 !!!"))
          File "C:/Users/Szymon/PycharmProjects/Testowanie Automatyczne/laboratorium-6-SzymonWilczewski/src/zad02/main.py", line 34, in ValidPassword
            raise ValueError
        ValueError
        """
        if ' ' in password:
            raise ValueError
        return bool(re.match(r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$', password))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
