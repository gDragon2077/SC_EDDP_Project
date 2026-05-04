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

# Metoda Runge-Kutta de ordinul 4
t_values = [t0]
rk4_values = [P0]

t = t0
P = P0

while t < t_final:
    K1 = h * f(t, P)
    K2 = h * f(t + h / 2, P + K1 / 2)
    K3 = h * f(t + h / 2, P + K2 / 2)
    K4 = h * f(t + h, P + K3)

    P = P + (K1 + 2*K2 + 2*K3 + K4) / 6
    t = t + h

    t_values.append(t)
    rk4_values.append(P)

# Tabel RK4
exact_values = [exact(t) for t in t_values]
errors = [abs(exact_values[i] - rk4_values[i]) for i in range(len(t_values))]

df_rk4 = pd.DataFrame({
    "n": range(len(t_values)),
    "t": t_values,
    "Runge-Kutta 4": rk4_values,
    "Solutie exacta": exact_values,
    "Eroare absoluta": errors
})

display(df_rk4.round(4))

# Grafic RK4
t_fine = np.linspace(t0, t_final, 300)
exact_fine = exact(t_fine)

plt.figure(figsize=(9, 5))

plt.plot(t_fine, exact_fine, label="Solutie exacta")
plt.plot(t_values, rk4_values, marker="o", linestyle="--", label="Runge-Kutta 4")

plt.title("Solutia exacta si aproximatia obtinuta prin metoda Runge-Kutta 4")
plt.xlabel("t")
plt.ylabel("P(t)")
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.show()