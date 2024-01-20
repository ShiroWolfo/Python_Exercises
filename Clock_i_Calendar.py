class Clock:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self._hours = self._validate_value(hours, 0, 23)
        self._minutes = self._validate_value(minutes, 0, 59)
        self._seconds = self._validate_value(seconds, 0, 59)

    def _validate_value(self, value, min_value, max_value):
        if min_value <= value <= max_value:
            return value
        else:
            raise ValueError(f"Invalid value: {value}. Value should be between {min_value} and {max_value}.")

    def set(self, hours=0, minutes=0, seconds=0):
        self._hours = self._validate_value(hours, 0, 23)
        self._minutes = self._validate_value(minutes, 0, 59)
        self._seconds = self._validate_value(seconds, 0, 59)

    def tick(self):
        self._seconds += 1
        if self._seconds >= 60:
            self._seconds = 0
            self._minutes += 1
            if self._minutes >= 60:
                self._minutes = 0
                self._hours += 1
                if self._hours >= 24:
                    self._hours = 0

    def display(self):
        print(f"{self._hours:02d}:{self._minutes:02d}:{self._seconds:02d}")

    def __str__(self):
        return f"{self._hours:02d}:{self._minutes:02d}:{self._seconds:02d}"

    def __repr__(self):
        return f"Clock({self._hours}, {self._minutes}, {self._seconds})"


class LeapYearDescriptor:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance._is_leap_year()

class Calendar:
    def __init__(self, day=1, month=1, year=1900):
        self._day = self._validate_value(day, 1, 31)
        self._month = self._validate_value(month, 1, 12)
        self._year = self._validate_value(year, 0, 9999)

    def _validate_value(self, value, min_value, max_value):
        if min_value <= value <= max_value:
            return value
        else:
            raise ValueError(f"Invalid value: {value}. Value should be between {min_value} and {max_value}.")

    def set(self, day=1, month=1, year=1900):
        self._day = self._validate_value(day, 1, 31)
        self._month = self._validate_value(month, 1, 12)
        self._year = self._validate_value(year, 0, 9999)

    def passage_of_time(self):
        months_with_31_days = [1, 3, 5, 7, 8, 10, 12]
        months_with_30_days = [4, 6, 9, 11]

        self._day += 1

        if self._day > 31 or (self._month in months_with_30_days and self._day > 30):
            self._day = 1
            self._month += 1

            if self._month > 12:
                self._month = 1
                self._year += 1

    is_leap_year = LeapYearDescriptor()

    def _is_leap_year(self):
        if self._year % 4 == 0:
            if self._year % 100 == 0:
                if self._year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

    def __str__(self):
        return f"{self._day:02d}/{self._month:02d}/{self._year}"

    def __repr__(self):
        return f"Calendar({self._day}, {self._month}, {self._year})"

# Przykładowe użycie
clock = Clock()
calendar = Calendar()

for _ in range(5):
    clock.tick()
    calendar.passage_of_time()

clock.set(10, 30, 45)
clock.display()  # Output: 10:30:45

clock.tick()
clock.display()
print(clock)
print(repr(clock))

print(calendar)  # Output: 06/01/1900
print(repr(calendar))  # Output: Calendar(6, 1, 1900)

calendar.set(31, 12, 2022)
print(calendar)
print(calendar.is_leap_year)  # Output: False
