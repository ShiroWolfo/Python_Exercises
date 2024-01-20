from abc import ABC, abstractmethod

class Temperature(ABC):
    def __init__(self, temperature):
        self._temperature = temperature

    @property
    @abstractmethod
    def temperature(self):
        pass

    @temperature.setter
    @abstractmethod
    def temperature(self, value):
        pass

    def __str__(self):
        return f"{self._temperature} stopni w skali Celsjusza"

    def __repr__(self):
        return f"{self.__class__.__name__}({self._temperature})"

    def above_freezing(self):
        return self._temperature > 0

    @abstractmethod
    def convert_to_Fahrenheit(self):
        pass

    @abstractmethod
    def convert_to_Celsius(self):
        pass

    @abstractmethod
    def convert_to_Kelvin(self):
        pass


class Fahrenheit(Temperature):
    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        self._temperature = value

    def convert_to_Fahrenheit(self):
        return self

    def convert_to_Celsius(self):
        celsius = 0.556 * (self._temperature - 32.0)
        return Celsius(celsius)

    def convert_to_Kelvin(self):
        celsius = self.convert_to_Celsius().temperature
        kelvin = celsius + 273.16
        return Kelvin(kelvin)


class Celsius(Temperature):
    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        self._temperature = value

    def convert_to_Fahrenheit(self):
        fahrenheit = (self._temperature / 0.556) + 32.0
        return Fahrenheit(fahrenheit)

    def convert_to_Celsius(self):
        return self

    def convert_to_Kelvin(self):
        kelvin = self._temperature + 273.16
        return Kelvin(kelvin)


class Kelvin(Temperature):
    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        self._temperature = value

    def convert_to_Fahrenheit(self):
        celsius = self.convert_to_Celsius().temperature
        fahrenheit = (celsius / 0.556) + 32.0
        return Fahrenheit(fahrenheit)

    def convert_to_Celsius(self):
        celsius = self._temperature - 273.16
        return Celsius(celsius)

    def convert_to_Kelvin(self):
        return self


# Listy zawierającej 12 instancji temperatur
temperatures = []
for _ in range(4):
    temperatures.append(Kelvin(300))
    temperatures.append(Celsius(25))
    temperatures.append(Fahrenheit(77))

# Wydrukowanie obiektów listy i dodanie adnotacji dla temperatur powyżej zera
for temp in temperatures:
    if temp.above_freezing():
        print(temp, "(powyżej zera)")
    else:
        print(temp)

# Listy z przekształconymi temperaturami
fahrenheit_list = [temp.convert_to_Fahrenheit() for temp in temperatures]
celsius_list = [temp.convert_to_Celsius() for temp in temperatures]
kelvin_list = [temp.convert_to_Kelvin() for temp in temperatures]

print()

# Temperatury poniżej temperatury zamarzania wody
freezing_celsius = Celsius(0)
freezing_fahrenheit = freezing_celsius.convert_to_Fahrenheit()
freezing_kelvin = freezing_celsius.convert_to_Kelvin()

below_freezing_fahrenheit = [temp for temp in fahrenheit_list if temp.temperature < freezing_fahrenheit.temperature]
below_freezing_celsius = [temp for temp in celsius_list if temp.temperature < freezing_celsius.temperature]
below_freezing_kelvin = [temp for temp in kelvin_list if temp.temperature < freezing_kelvin.temperature]

print("Temperatury poniżej temperatury zamarzania wody:")
print("Fahrenheit:", below_freezing_fahrenheit)
print("Celsius:", below_freezing_celsius)
print("Kelvin:", below_freezing_kelvin)