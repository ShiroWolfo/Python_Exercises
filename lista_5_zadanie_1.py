class Fraction:
    def __init__(self, numerator, denominator):
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("Licznik i Mianownik muszą być całkowite")
        if denominator == 0:
            raise ValueError("Mianownik nie może się równać 0")
        self._numerator = numerator
        self._denominator = denominator
        self._simplify()

    @property
    def numerator(self):
        return self._numerator

    @property
    def denominator(self):
        return self._denominator

    def _simplify(self):
        common_divisor = self._gcd(self._numerator, self._denominator)
        self._numerator //= common_divisor
        self._denominator //= common_divisor
        if self._denominator < 0:
            self._numerator *= -1
            self._denominator *= -1

    def _gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self._numerator == other.numerator and self._denominator == other.denominator
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if isinstance(other, Fraction):
            return self._numerator * other.denominator < other.numerator * self._denominator
        raise TypeError("Cannot compare Fraction with non-Fraction type")

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        return not self.__le__(other)

    def __ge__(self, other):
        return not self.__lt__(other)

    def __add__(self, other):
        if isinstance(other, Fraction):
            numerator = (self._numerator * other.denominator) + (other.numerator * self._denominator)
            denominator = self._denominator * other.denominator
            return Fraction(numerator, denominator)
        raise TypeError("Cannot add Fraction with non-Fraction type")

    def __sub__(self, other):
        if isinstance(other, Fraction):
            numerator = (self._numerator * other.denominator) - (other.numerator * self._denominator)
            denominator = self._denominator * other.denominator
            return Fraction(numerator, denominator)
        raise TypeError("Cannot subtract Fraction with non-Fraction type")

    def __mul__(self, other):
        if isinstance(other, Fraction):
            numerator = self._numerator * other.numerator
            denominator = self._denominator * other.denominator
            return Fraction(numerator, denominator)
        raise TypeError("Cannot multiply Fraction with non-Fraction type")

    def __truediv__(self, other):
        if isinstance(other, Fraction):
            numerator = self._numerator * other.denominator
            denominator = self._denominator * other.numerator
            return Fraction(numerator, denominator)
        raise TypeError("Cannot divide Fraction with non-Fraction type")

    def __str__(self):
        return f"{self._numerator}/{self._denominator}"

    def __repr__(self):
        return f"Fraction({self._numerator}, {self._denominator})"

    def __float__(self):
        return self._numerator / self._denominator

    def __getitem__(self, index):
        if index == 0:
            return self._numerator
        elif index == 1:
            return self._denominator
        raise IndexError("Fraction index out of range")


# Przykładowe użycie
frac1 = Fraction(3, 4)
frac2 = Fraction(1, 2)

print(frac1)  # Wyświetlenie ułamka
print(repr(frac2))  # Reprezentacja ułamka

print(frac1 == frac2)  # Porównanie ułamków
print(frac1 + frac2)  # Dodawanie ułamków
print(frac1 - frac2)  # Odejmowanie ułamków
print(frac1 * frac2)  # Mnożenie ułamków
print(frac1 / frac2)  # Dzielenie ułamków

print(float(frac1))  # Przekształcenie ułamka na float

print(frac1[0])  # Odczytanie licznika
print(frac2[1])  # Odczytanie mianownika