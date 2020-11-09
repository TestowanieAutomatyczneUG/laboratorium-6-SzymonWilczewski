import doctest


class Hamming:
    def distance(self, str1, str2):
        """
        >>> hamming = Hamming()
        >>> hamming.distance("", "")
        0
        >>> hamming.distance("A", "A")
        0
        >>> hamming.distance("G", "T")
        1
        >>> hamming.distance("GGACTGAAATCTG", "GGACTGAAATCTG")
        0
        >>> hamming.distance("GGACGGATTCTG", "AGGACGGATTCT")
        9
        >>> hamming.distance("AATG", "AAA")
        Traceback (most recent call last):
          File "C:/Users/Szymon/PycharmProjects/Testowanie Automatyczne/laboratorium-6-SzymonWilczewski/src/zad01/main.py", line 107, in <module>
            print(Hamming.distance(Hamming, "AATG", "AAA"))
          File "C:/Users/Szymon/PycharmProjects/Testowanie Automatyczne/laboratorium-6-SzymonWilczewski/src/zad01/main.py", line 99, in distance
            raise ValueError("Strands must have the same length!")
        ValueError: Strands must have the same length!
        >>> hamming.distance("ATA", "AGTG")
        Traceback (most recent call last):
          File "C:/Users/Szymon/PycharmProjects/Testowanie Automatyczne/laboratorium-6-SzymonWilczewski/src/zad01/main.py", line 41, in <module>
            print(Hamming.distance(Hamming, "ATA", "AGTG"))
          File "C:/Users/Szymon/PycharmProjects/Testowanie Automatyczne/laboratorium-6-SzymonWilczewski/src/zad01/main.py", line 33, in distance
            raise ValueError("Strands must have the same length!")
        ValueError: Strands must have the same length!
        >>> hamming.distance("", "G")
        Traceback (most recent call last):
          File "C:/Users/Szymon/PycharmProjects/Testowanie Automatyczne/laboratorium-6-SzymonWilczewski/src/zad01/main.py", line 46, in <module>
            print(Hamming.distance(Hamming, "", "G"))
          File "C:/Users/Szymon/PycharmProjects/Testowanie Automatyczne/laboratorium-6-SzymonWilczewski/src/zad01/main.py", line 38, in distance
            raise ValueError("Strands must have the same length!")
        ValueError: Strands must have the same length!
        >>> hamming.distance("G", "")
        Traceback (most recent call last):
          File "C:/Users/Szymon/PycharmProjects/Testowanie Automatyczne/laboratorium-6-SzymonWilczewski/src/zad01/main.py", line 51, in <module>
            print(Hamming.distance(Hamming, "G", ""))
          File "C:/Users/Szymon/PycharmProjects/Testowanie Automatyczne/laboratorium-6-SzymonWilczewski/src/zad01/main.py", line 43, in distance
            raise ValueError("Strands must have the same length!")
        ValueError: Strands must have the same length!
        """
        if len(str1) != len(str2):
            raise ValueError("Strands must have the same length!")
        diff = 0
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                diff += 1
        return diff


if __name__ == "__main__":
    import doctest
    doctest.testmod()
