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

# Metoda Euler
t_values = [t0]
euler_values = [P0]

t = t0
P = P0

while t < t_final:
    P = P + h * f(t, P)
    t = t + h

    t_values.append(t)
    euler_values.append(P)

# Tabel Euler
exact_values = [exact(t) for t in t_values]
errors = [abs(exact_values[i] - euler_values[i]) for i in range(len(t_values))]

df_euler = pd.DataFrame({
    "n": range(len(t_values)),
    "t": t_values,
    "Euler": euler_values,
    "Solutie exacta": exact_values,
    "Eroare absoluta": errors
})

display(df_euler.round(4))

# Grafic Euler
t_fine = np.linspace(t0, t_final, 300)
exact_fine = exact(t_fine)

plt.figure(figsize=(9, 5))

plt.plot(t_fine, exact_fine, label="Solutie exacta")
plt.plot(t_values, euler_values, marker="o", linestyle="--", label="Euler")

plt.title("Solutia exacta si aproximatia obtinuta prin metoda Euler")
plt.xlabel("t")
plt.ylabel("P(t)")
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.show()