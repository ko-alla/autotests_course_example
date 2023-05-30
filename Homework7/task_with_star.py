from enum import Enum

class RomanNums(Enum):
    M  = 1000
    CM = 900
    D  = 500
    CD = 400
    C  = 100
    XC = 90
    L  = 50
    XL = 40
    X  = 10
    IX = 9
    V  = 5
    IV = 4
    I  = 1

    @classmethod
    def from_roman(cls, n):
        for numeral in cls:
            rep, n = divmod(n, numeral.value)
            yield numeral.name * rep