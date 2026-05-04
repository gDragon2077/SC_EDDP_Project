import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Datele problemei
a = 0.6
V = 70
P0 = 100

t0 = 0
t_final = 5
h = 0.5

# Functia din ecuatia diferentiala
def f(t, P):
    return a * (V - P)

# Solutia exacta
def exact(t):
    return V + (P0 - V) * np.exp(-a * t)

# Metoda Heun
t_values = [t0]
heun_values = [P0]

t = t0
P = P0

while t < t_final:
    K1 = h * f(t, P)
    K2 = h * f(t + h, P + K1)

    P = P + (K1 + K2) / 2
    t = t + h

    t_values.append(t)
    heun_values.append(P)

# Tabel Heun
exact_values = [exact(t) for t in t_values]
errors = [abs(exact_values[i] - heun_values[i]) for i in range(len(t_values))]

df_heun = pd.DataFrame({
    "n": range(len(t_values)),
    "t": t_values,
    "Heun": heun_values,
    "Solutie exacta": exact_values,
    "Eroare absoluta": errors
})

display(df_heun.round(4))

# Grafic Heun
t_fine = np.linspace(t0, t_final, 300)
exact_fine = exact(t_fine)

plt.figure(figsize=(9, 5))

plt.plot(t_fine, exact_fine, label="Solutie exacta")
plt.plot(t_values, heun_values, marker="o", linestyle="--", label="Heun")

plt.title("Solutia exacta si aproximatia obtinuta prin metoda Heun")
plt.xlabel("t")
plt.ylabel("P(t)")
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.show()