# Mój 2
import numpy as np

# Funkcja do wygodnego wyświetlania jednowymiarowych tablic 8x8
def print_friendly(arr):
    for i in range(1, 65):
        print(arr[i - 1], end=" ")
        if i % 8 == 0:
            print()

# Inicjalizacja danych wejściowych do nauki - tablicy 64 elementów
def initialize_input_array():
    x = [0 if i % 2 == 0 else 1 for i in range(64)]
    return x

# Inicjalizacja macierzy na podstawie wzoru z algorytmu Hopfielda
def initialize_matrix(x):
    matrix = np.zeros((64, 64), dtype=int)

    for i in range(64):
        for j in range(64):
            if i == j:
                matrix[i][j] = 0
            else:
                # Wzór z algorytmu Hopfielda
                result = (2 * x[i] - 1) * (2 * x[j] - 1)
                matrix[i][j] = result

    return matrix

# Funkcja do pobierania danych od użytkownika w interaktywny sposób
def user_input():
    x2 = np.zeros(64, dtype=int)

    for i in range(8):
        row_input = input(f"Podaj wiersz {i+1} (8 liczb oddzielonych spacją): ")
        row_values = list(map(int, row_input.split()))
        x2[i*8:(i+1)*8] = row_values

    return x2

# Obliczenia na podstawie danych wejściowych, macierzy i wzoru z algorytmu Hopfielda
def calculate_result(x2, matrix):
    s_array = []
    for i in range(64):
        result = 0
        for j in range(64):
            result += x2[j] * matrix[i][j]
        s_array.append(result)

    # Wyniki są przekazywane do funkcji aktywacyjnej
    output = [1 if s > 0 else 0 for s in s_array]
    return output

# Główna część programu
if __name__ == "__main__":
    # Inicjalizacja danych wejściowych, macierzy i danych od użytkownika
    x = initialize_input_array()
    matrix = initialize_matrix(x)
    x2 = user_input()

    # Obliczenia i wyświetlanie wyników
    output = calculate_result(x2, matrix)
    print("Dane wejściowe do nauki:")
    print_friendly(x)
    print("\n\nDane wejściowe od użytkownika:")
    print_friendly(x2)
    print("\n\nWynik:")
    print_friendly(output)

    input()  # Czekaj na dowolny klawisz przed zakończeniem