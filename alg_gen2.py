import random
import numpy as np
# import matplotlib.pyplot as plt


def f(x, a, b, c, d):
    return a * x ** 3 + b * x ** 2 + c * x + d

def f_celu(chromosom, punkty):
    blad = np.sum((f(x, *chromosom) - y) ** 2 for x, y in punkty)
    return blad

def krzyzowanie(rodzic1, rodzic2):
    punkt_krzyzowania = random.randint(1, len(rodzic1) - 1)
    dzi_1 = np.concatenate((rodzic1[:punkt_krzyzowania], rodzic2[punkt_krzyzowania:]))
    dzi_2 = np.concatenate((rodzic2[:punkt_krzyzowania], rodzic1[punkt_krzyzowania:]))
    return dzi_1, dzi_2, punkt_krzyzowania

def mutacja(chromosom, wspol_mutacji):
    zmutowane_indeksy = np.random.rand(len(chromosom)) < wspol_mutacji
    chromosom[zmutowane_indeksy] += np.random.randint(-1, 2, size=np.sum(zmutowane_indeksy))
    return chromosom

def algorytm_genetyczny(punkty, roz_pop=100, gen=100, wsp_mutacji=0.1):
    pop = np.random.randint(-15, 15, size=(roz_pop, 4))

    for generacja in range(gen):
        wyniki = np.array([f_celu(chromosom.astype(int), punkty) for chromosom in pop])
        naj_indeks = np.argmin(wyniki)
        naj_chromosom = pop[naj_indeks]
        naj_cel = f_celu(naj_chromosom.astype(float), punkty)
        print(f"Generacja: {generacja + 1}")
        znormalizowane_wyniki = 1 / (1 + wyniki)
        wyb_indeksy = np.random.choice(np.arange(roz_pop), size=roz_pop, replace=True, p=znormalizowane_wyniki / np.sum(znormalizowane_wyniki))
        wybrana_pop = pop[wyb_indeksy]

        potomstwo = []
        for _ in range(roz_pop // 2):
            rodzic1, rodzic2 = np.random.choice(wyb_indeksy, size=2, replace=False)
            dzi_1, dzi_2, punkt_krzyzowania = krzyzowanie(wybrana_pop[rodzic1], wybrana_pop[rodzic2])
            dzi_1 = mutacja(dzi_1, wsp_mutacji)
            dzi_2 = mutacja(dzi_2, wsp_mutacji)
            potomstwo.extend([dzi_1, dzi_2])
        wynik = np.array([f_celu(chromosom.astype(float), punkty) for chromosom in potomstwo])
        print("Punkt krzyżowania: ", punkt_krzyzowania)
        print("Rodzic 1: ", wybrana_pop[rodzic1])
        print("Rodzic 2: ", wybrana_pop[rodzic2])
        print("Dziecko 1", dzi_1)
        print("Dziecko 2", dzi_2)
        print(f"Wartość celu = {int(round(naj_cel))}")
        for i in range(roz_pop):
            if wynik[i] < wyniki[wyb_indeksy[i]]:
                pop[wyb_indeksy[i]] = potomstwo[i]

    naj_indeks = np.argmin(wyniki)
    naj_chromosom = pop[naj_indeks]

    return naj_chromosom

# def wykres(punkty, najlepszy_chromosom):
#     x_wartosci = np.linspace(min(punkty[:, 0]), max(punkty[:, 0]), 100)
#     y_wartosci = f(x_wartosci, *najlepszy_chromosom)
#     plt.scatter(punkty[:, 0], punkty[:, 1], label='Dane')
#     plt.plot(x_wartosci, y_wartosci, color='red', label='Funkcja: a * x ^ 3 + b * x ^ 2 + c * x + d')
#     plt.xlabel('x')
#     plt.ylabel('y')
#     plt.legend()
#     plt.title('Dopasowanie funkcji do danych')
#     plt.grid(True)
#     plt.show()

punkty = np.array([(-5, -150), (-4, -77), (-3, -30), (-2, 0), (-1, 10), (1 / 2, 131 / 8), (1, 18), (2, 25), (3, 32), (4, 75), (5, 130)])

naj_chromosom = algorytm_genetyczny(punkty)
a, b, c, d = naj_chromosom
print("Najlepsze współczynniki: a={}, b={}, c={}, d={}".format(a, b, c, d))
# wykres(punkty, naj_chromosom)
input()