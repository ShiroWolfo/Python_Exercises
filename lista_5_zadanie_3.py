#LISTA 5
#ZADANIE3---------------------------------------------------------------------------------------------------
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


#ZADANIE3---------------------------------------------------------------------------------------------------

class QuadraticEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        if value == 0:
            raise ValueError("Coefficient 'a' cannot be zero")
        self._a = float(value)

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        self._b = float(value)

    @property
    def c(self):
        return self._c

    @c.setter
    def c(self, value):
        self._c = float(value)

    @property
    def delta(self):
        return self.b**2 - 4*self.a*self.c

    def roots(self):
        delta = self.delta
        if delta > 0:
            x1 = (-self.b + delta**0.5) / (2*self.a)
            x2 = (-self.b - delta**0.5) / (2*self.a)
            return x1, x2
        elif delta == 0:
            x = -self.b / (2*self.a)
            return x,
        else:
            return ()

    def factored_form(self):
        if self.a == 0:
            return "postać iloczynowa nie istnieje"
        elif self.delta == 0:
            x = -self.b / (2*self.a)
            return f"(x - {x})^2"
        elif self.delta > 0:
            x1 = (-self.b + self.delta**0.5) / (2*self.a)
            x2 = (-self.b - self.delta**0.5) / (2*self.a)
            return f"(x - {x1})(x - {x2})"
        else:
            return "postać iloczynowa nie istnieje"

    def __call__(self, x):
        return self.a*x**2 + self.b*x + self.c

    def __add__(self, other):
        if isinstance(other, QuadraticEquation):
            a = self.a + other.a
            b = self.b + other.b
            c = self.c + other.c
            return QuadraticEquation(a, b, c)
        raise TypeError("Cannot add QuadraticEquation with non-QuadraticEquation type")

    def __sub__(self, other):
        if isinstance(other, QuadraticEquation):
            a = self.a - other.a
            b = self.b - other.b
            c = self.c - other.c
            return QuadraticEquation(a, b, c)
        raise TypeError("Cannot subtract QuadraticEquation with non-QuadraticEquation type")

    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            a = self.a * scalar
            b = self.b * scalar
            c = self.c * scalar
            return QuadraticEquation(a, b, c)
        raise TypeError("Cannot multiply QuadraticEquation with non-numeric type")

    def __str__(self):
        return f"y = {self.a}x^2 + {self.b}x + {self.c}"

    def __repr__(self):
        return f"QuadraticEquation({self.a}, {self.b}, {self.c})"

class Menu:
    def __init__(self):
        self.equation = None

    def display_menu(self):
        print("1. Utwórz równanie kwadratowe")
        print("2. Oblicz deltę")
        print("3. Oblicz pierwiastki równania")
        print("4. Wyświetl postać iloczynową równania")
        print("5. Oblicz wartość dla podanego x")
        print("6. Dodaj równanie")
        print("7. Odejmij równanie")
        print("8. Pomnóż równanie przez skalar")
        print("9. Wyświetl równanie")
        print("0. Wyjście")

    def create_equation(self):
        a = float(input("Podaj wartość a: "))
        b = float(input("Podaj wartość b: "))
        c = float(input("Podaj wartość c: "))
        try:
            self.equation = QuadraticEquation(a, b, c)
            print("Równanie zostało utworzone")
        except ValueError as e:
            print(str(e))

    def calculate_delta(self):
        if self.equation is not None:
            print(f"Delta równania: {self.equation.delta}")
        else:
            print("Nie utworzono równania")

    def calculate_roots(self):
        if self.equation is not None:
            roots = self.equation.roots()
            if len(roots) > 0:
                print(f"Pierwiastki równania: {', '.join(str(root) for root in roots)}")
            else:
                print("Równanie nie posiada pierwiastków")
        else:
            print("Nie utworzono równania")

    def display_factored_form(self):
        if self.equation is not None:
            print(f"Postać iloczynowa równania: {self.equation.factored_form()}")
        else:
            print("Nie utworzono równania")

    def calculate_value(self):
        if self.equation is not None:
            x = float(input("Podaj wartość x: "))
            value = self.equation(x)
            print(f"Wartość dla x = {x}: {value}")
        else:
            print("Nie utworzono równania")

    def add_equation(self):
        if self.equation is not None:
            a = float(input("Podaj wartość a: "))
            b = float(input("Podaj wartość b: "))
            c = float(input("Podaj wartość c: "))
            try:
                other = QuadraticEquation(a, b, c)
                self.equation += other
                print("Równanie zostało dodane")
            except ValueError as e:
                print(str(e))
            except TypeError as e:
                print(str(e))
        else:
            print("Nie utworzono równania")

    def subtract_equation(self):
        if self.equation is not None:
            a = float(input("Podaj wartość a: "))
            b = float(input("Podaj wartość b: "))
            c = float(input("Podaj wartość c: "))
            try:
                other = QuadraticEquation(a, b, c)
                self.equation -= other
                print("Równanie zostało odjęte")
            except ValueError as e:
                print(str(e))
            except TypeError as e:
                print(str(e))
        else:
            print("Nie utworzono równania")

    def multiply_by_scalar(self):
        if self.equation is not None:
            scalar = float(input("Podaj wartość skalar: "))
            self.equation *= scalar
            print("Równanie zostało pomnożone przez skalar")
        else:
            print("Nie utworzono równania")

    def display_equation(self):
        if self.equation is not None:
            print(self.equation)
        else:
            print("Nie utworzono równania")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Wybierz opcję: ")
            if choice == "1":
                self.create_equation()
            elif choice == "2":
                self.calculate_delta()
            elif choice == "3":
                self.calculate_roots()
            elif choice == "4":
                self.display_factored_form()
            elif choice == "5":
                self.calculate_value()
            elif choice == "6":
                self.add_equation()
            elif choice == "7":
                self.subtract_equation()
            elif choice == "8":
                self.multiply_by_scalar()
            elif choice == "9":
                self.display_equation()
            elif choice == "0":
                break
            else:
                print("Niepoprawny wybór. Spróbuj ponownie.")


menu = Menu()
menu.run()
