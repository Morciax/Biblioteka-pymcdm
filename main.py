import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pymcdm.methods import TOPSIS, VIKOR, SPOTIS, PROMETHEE_II
from pymcdm.helpers import rankdata
# Dane przykładowe
data = {
    'Kryterium 1': [4, 7, 3, 5],
    'Kryterium 2': [2, 9, 4, 6],
    'Kryterium 3': [6, 3, 8, 5]
}
alternatives = ['A1', 'A2', 'A3', 'A4']
criteria = ['Kryterium 1', 'Kryterium 2', 'Kryterium 3']
df = pd.DataFrame(data, index=alternatives)

# Macierz decyzyjna
matrix = df.values

# Normalizacja danych Min-Max
def normalize_min_max(matrix):
    min_vals = np.min(matrix, axis=0)
    max_vals = np.max(matrix, axis=0)
    return (matrix - min_vals) / (max_vals - min_vals)

normalized_matrix = normalize_min_max(matrix)

# Wagi i typy kryteriów
weights = np.array([0.3, 0.5, 0.2])
types = np.array([1, 1, 1])

# Określenie granic dla SPOTIS po normalizacji
bounds = np.array([[0, 1]] * matrix.shape[1])

# Metody MCDM
methods = {
    'TOPSIS': TOPSIS(),
    'VIKOR': VIKOR(),
    'SPOTIS': SPOTIS(bounds=bounds),
    'PROMETHEE_II': PROMETHEE_II(preference_function='usual')
}
scores_dict = {}
ranks_dict = {}

print("Wyniki MCDM:\n")
for name, method in methods.items():
    scores = method(normalized_matrix, weights, types)
    ranks = rankdata(scores, reverse=True)

    scores_dict[name] = scores
    ranks_dict[name] = ranks

    print(f"{name}:\nOceny: {scores}\nRangi: {ranks}\n")

results_df = pd.DataFrame(scores_dict, index=alternatives)

plt.figure(figsize=(10, 6))
for method, scores in scores_dict.items():
    plt.plot(alternatives, scores, label=method, marker='o')

plt.title('Porównanie wyników MCDM dla różnych metod')
plt.xlabel('Alternatywy')
plt.ylabel('Oceny')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Wizualizacja rankingu
plt.figure(figsize=(10, 6))
for method, ranks in ranks_dict.items():
    plt.plot(alternatives, ranks, label=method, marker='x')

plt.title('Porównanie rang MCDM dla różnych metod')
plt.xlabel('Alternatywy')
plt.ylabel('Rangi')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


