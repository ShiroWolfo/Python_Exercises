import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Załaduj zestaw danych IRIS
iris = datasets.load_iris()
X, y = iris.data, iris.target

# Podziel dane na zbiór treningowy i testowy
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Implementacja algorytmu K-Nearest Neighbors
def knn_classifier(train_data, train_labels, test_data, k):
    predictions = []
    for test_point in test_data:
        distances = np.linalg.norm(train_data - test_point, axis=1)
        nearest_neighbors = np.argsort(distances)[:k]
        most_common_label = np.bincount(train_labels[nearest_neighbors]).argmax()
        predictions.append(most_common_label)
    return predictions


# Przetestuj różne wartości k
k_values = [3, 5, 7]

# Szkic sprawozdania
print("Sprawozdanie - Klasyfikacja danych przy użyciu KNN\n")

# 1. Wprowadzenie
print("1. Wprowadzenie:")
print("   Projekt ma na celu klasyfikację danych przy użyciu algorytmu K-Nearest Neighbors (KNN).\n")

# 2. Opis zbioru danych
print("2. Opis zbioru danych:")
print("   Zbiór danych użyty do projektu to IRIS dataset, zawierający informacje o cechach kwiatów IRIS.\n")

# 3. Metodologia
print("3. Metodologia:")
print("   Dane zostały podzielone na zbiór treningowy i testowy. Testowane są różne wartości k dla algorytmu KNN.\n")

# 4. Implementacja
print("4. Implementacja:")
for k in k_values:
    print(f"\nKNN (k={k}):")
    predictions = knn_classifier(X_train, y_train, X_test, k)

    # Wypisz predykcje dla każdej próbki testowej
    print("   Predykcje dla próbek testowych:")
    for i, pred in enumerate(predictions):
        print(f"   Próbka {i + 1}: Predykcja={pred}, Oczekiwana={y_test[i]}")

    # Wypisz dokładność klasyfikacji
    accuracy = accuracy_score(y_test, predictions)
    print(f"\n   Dokładność klasyfikacji: {accuracy:.2f}")

    # Wypisz macierz pomyłek
    cm = confusion_matrix(y_test, predictions)
    print("\n   Macierz pomyłek:")
    print(cm)

    # Wypisz raport klasyfikacyjny
    cr = classification_report(y_test, predictions, target_names=iris.target_names)
    print("\n   Raport klasyfikacyjny:")
    print(cr)

# 5. Podsumowanie
print("\n5. Podsumowanie:")
print(
    "   Projekt demonstrował klasyfikację danych za pomocą algorytmu KNN. Wyniki dla różnych wartości k zostały przeanalizowane.")
