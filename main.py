import random
#Wartości tablocy
x1 = [0, 0, 1, 1]
x2 = [0, 1, 0, 1]
x3 = [1, 1, 1, 1]

#Wagi
w1 = random.uniform(-1, 1)
w2 = random.uniform(-1, 1)
w3 = random.uniform(-1, 1)

s = 0
i = 0

#Tablice
y = [0, 0, 0, 0]
d = [0, 1, 1, 1]
delta = [1, 1, 1, 1]

#Współczynnik uczenia
wu = float(input("Podaj Wu z przedziału od -1 do 1 : "))

#Pętla działająca do momentu uzyskania poprawnego wyniku
while delta != [0, 0, 0, 0]:
    #Pętla wyliczająca wartości sprawdzane
    for i in range(4):
        s = x1[i] * w1 + x2[i] * w2 + x3[i] * w3
        #Warunek sprawdzający zakres w którym dana wartość się znajduje i przypisuje do nich wartość wynikową
        if s <= 0:
            y[i] = 0
        else:
            y[i] = 1
        #Wyliczanie błędy
        delta[i] = d[i] - y[i]
        #Nadawanie nowych wag
        w1 = w1 + x1[i] * wu * delta[i]
        w2 = w2 + x2[i] * wu * delta[i]
        w3 = w3 + x3[i] * wu * delta[i]



print("waga 1 = ", round(w1, 1), "waga 2 = ", round(w2, 1), "waga 3 = ", round(w3, 1), "wspolczynnik uczenia = ", wu)
print("delta = ", delta, "y = ", y, "Wartosc docelowa = ", d)

a = input()