import matplotlib.pyplot as plt
import pandas as pd

# Caricamento del dataset
df = pd.read_csv("winequality-red.csv", sep=",")

# Definizione di x e y
x = df["quality"].value_counts().sort_index().index
y = df["quality"].value_counts().sort_index().values

plt.title("Distribuzione della qualità del vino rosso")
plt.xlabel("Qualità")
plt.ylabel("Numero di vini")

plt.xticks(x)
plt.show()
