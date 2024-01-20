from collections.abc import Sequence

class SortedList(Sequence):
    def __init__(self, key=None):
        self._key = key
        self._data = []

    @property
    def key(self):
        return self._key

    def clear(self):
        self._data.clear()

    def _find_index(self, value):
        low = 0
        high = len(self._data)
        while low < high:
            mid = (low + high) // 2
            if self._data[mid] < value:
                low = mid + 1
            else:
                high = mid
        return low

    def add(self, value):
        index = self._find_index(value)
        self._data.insert(index, value)

    def pop(self, index=-1):
        return self._data.pop(index)

    def remove(self, value):
        self._data.remove(value)

    def remove_every(self, value):
        while value in self._data:
            self._data.remove(value)

    def __delitem__(self, index):
        del self._data[index]

    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, index, value):
        self._data[index] = value

    def __iter__(self):
        return iter(self._data)

    def __reversed__(self):
        return reversed(self._data)

    def __contains__(self, value):
        return value in self._data

    def __len__(self):
        return len(self._data)

    def __str__(self):
        return str(self._data)

    def copy(self):
        return self._data.copy()

    def __copy__(self):
        return SortedList(self._key)

    def extend(self, values):
        self._data.extend(values)
        self._data.sort(key=self._key)

    def count(self, value):
        return self._data.count(value)

    def index(self, value, start=None, end=None):
        return self._data.index(value, start, end)


sorted_list = SortedList(key=lambda x: x.lower())  # Tworzenie posortowanej listy na podstawie klucza sortowania (ignorowanie wielkości liter)

sorted_list.add("apple")
sorted_list.add("banana")
sorted_list.add("cherry")
sorted_list.add("banana")  # Dodanie tego samego elementu

print(sorted_list)  # Wydrukowanie posortowanej listy

sorted_list.remove("cherry")  # Usunięcie elementu
print(sorted_list)

print("banana" in sorted_list)  # Sprawdzenie czy element jest w liście

sorted_list.extend(["orange", "kiwi"])  # Rozszerzenie listy o nowe elementy
print(sorted_list)

print(sorted_list.index("banana"))  # Indeks elementu w liście
