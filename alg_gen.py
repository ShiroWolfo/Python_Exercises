import random
import numpy as np
from matplotlib import pyplot as plt


def f(x, a, b, c, d):
    return a * x ** 3 + b * x ** 2 + c * x + d


def f_celu(chromosom, punkty):
    blad = 0
    for punkt in punkty:
        x, y = punkt
        blad += (f(x, *chromosom) - y) ** 2
    return 1 / (blad + 1e-10) + 106


def selekcja_ruletka(populacja, oceny):
    suma_ocen = sum(oceny)
    prawdopodobienstwa = [ocena / suma_ocen for ocena in oceny]
    wybrane_indeksy = random.choices(range(len(populacja)), weights=prawdopodobienstwa, k=len(populacja))
    wybrana_populacja = [populacja[i] for i in wybrane_indeksy]
    return wybrana_populacja


def krzyzowanie(rodzic1, rodzic2):
    indeks = random.randint(0, len(rodzic1) - 1)
    dziecko1 = rodzic1[:indeks] + rodzic2[indeks:]
    dziecko2 = rodzic2[:indeks] + rodzic1[indeks:]
    return dziecko1, dziecko2, indeks  # Dodano zwracanie punktu krzyżowania


def mutacja(chromosom, wspolczynnik_mutacji):
    zmutowany_chromosom = chromosom.copy()
    for i in range(len(zmutowany_chromosom)):
        if random.random() < wspolczynnik_mutacji:
            zmutowany_chromosom[i] += round(random.uniform(-1, 1))
            zmutowany_chromosom[i] = max(-15, min(15, zmutowany_chromosom[i]))
    return zmutowany_chromosom


def algorytm_genetyczny(punkty, rozmiar_populacji, wspolczynnik_mutacji, generacje):
    populacja = [[random.randint(-15, 15) for _ in range(4)] for _ in range(rozmiar_populacji)]

    for generacja in range(generacje):
        oceny = [f_celu(chromosom, punkty) for chromosom in populacja]
        najlepszy_chromosom = populacja[oceny.index(max(oceny))]
        wybrana_populacja = selekcja_ruletka(populacja, oceny)

        nowa_populacja = [najlepszy_chromosom]
        while len(nowa_populacja) < rozmiar_populacji:
            rodzic1, rodzic2 = random.choices(wybrana_populacja, k=2)
            dziecko1, dziecko2, punkt_krzyzowania = krzyzowanie(rodzic1, rodzic2)
            dziecko1_zmutowane = mutacja(dziecko1, wspolczynnik_mutacji)
            dziecko2_zmutowane = mutacja(dziecko2, wspolczynnik_mutacji)
            nowa_populacja.extend([dziecko1_zmutowane, dziecko2_zmutowane])

        populacja = nowa_populacja
        najlepsza_ocena = max(oceny)
        print(f"Generacja: {generacja + 1}")
        print("Punkt Krzyżowania:", punkt_krzyzowania)
        print("Rodzic1: ", rodzic1)
        print("Rodzic2: ", rodzic2)
        print("Dziecko1", dziecko1)
        print("Dziecko2", dziecko2)
        print("Mutacja w Dziecku1: ", dziecko1, " -> ", dziecko1_zmutowane)
        print("Mutacja w Dziecku2: ", dziecko2, " -> ", dziecko2_zmutowane)
        print(f"Wartość celu: {int(round(najlepsza_ocena))}")
    return najlepszy_chromosom


punkty = [(-5, -150), (-4, -77), (-3, -30), (-2, 0), (-1, 10), (1 / 2, 131 / 8), (1, 18), (2, 25), (3, 32), (4, 75),
          (5, 130)]
najlepszy_chromosom = algorytm_genetyczny(punkty, rozmiar_populacji=10, wspolczynnik_mutacji=0.1, generacje=1000)
print(f"Najlepszy chromosom: {najlepszy_chromosom}")

x_punkty, y_punkty = zip(*punkty)
x_wartosci = np.linspace(min(x_punkty), max(x_punkty), 100)
y_wartosci = f(x_wartosci, a=najlepszy_chromosom[0], b=najlepszy_chromosom[1],
               c=najlepszy_chromosom[2], d=najlepszy_chromosom[3])

plt.plot(x_wartosci, y_wartosci,
         label=f'Funkcja: {najlepszy_chromosom[0]}x^3 + {najlepszy_chromosom[1]}x^2 + {najlepszy_chromosom[2]}x + {najlepszy_chromosom[3]}')
plt.scatter(x_punkty, y_punkty, color='red', label='Wybrane punkty')

plt.xlabel('x')
plt.ylabel('Wartość Funkcji')
plt.title('Wykres Funkcji')

plt.grid(True)
plt.legend()
plt.show()
input("Naciśnij Enter, aby zakońćzyć program...")
