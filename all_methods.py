import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Datele problemei

a = 0.6
V = 70
P0 = 100

r0 = 0
r_final = 5
h = 0.5

# Functia ecuatiei diferentiale si solutia exacta

def f(r, P):
    return a * (V - P)

def exact(r):
    return V + (P0 - V) * np.exp(-a * r)

# Metoda Euler

def euler_method():
    r_values = [r0]
    P_values = [P0]

    r = r0
    P = P0

    while r < r_final:
        P = P + h * f(r, P)
        r = r + h

        r_values.append(r)
        P_values.append(P)

    return r_values, P_values

# Metoda Heun

def heun_method():
    r_values = [r0]
    P_values = [P0]

    r = r0
    P = P0

    while r < r_final:
        K1 = h * f(r, P)
        K2 = h * f(r + h, P + K1)

        P = P + (K1 + K2) / 2
        r = r + h

        r_values.append(r)
        P_values.append(P)

    return r_values, P_values

# Metoda Runge-Kutta 4

def rk4_method():
    r_values = [r0]
    P_values = [P0]

    r = r0
    P = P0

    while r < r_final:
        K1 = h * f(r, P)
        K2 = h * f(r + h / 2, P + K1 / 2)
        K3 = h * f(r + h / 2, P + K2 / 2)
        K4 = h * f(r + h, P + K3)

        P = P + (K1 + 2*K2 + 2*K3 + K4) / 6
        r = r + h

        r_values.append(r)
        P_values.append(P)

    return r_values, P_values

# Calcularea valorilor

r_values, euler_values = euler_method()
_, heun_values = heun_method()
_, rk4_values = rk4_method()

exact_values = [exact(r) for r in r_values]

error_euler = [abs(exact_values[i] - euler_values[i]) for i in range(len(r_values))]
error_heun = [abs(exact_values[i] - heun_values[i]) for i in range(len(r_values))]
error_rk4 = [abs(exact_values[i] - rk4_values[i]) for i in range(len(r_values))]

# Tabel comparativ final

df_compare = pd.DataFrame({
    "n": range(len(r_values)),
    "r": r_values,
    "Exacta": exact_values,
    "Euler": euler_values,
    "Eroare Euler": error_euler,
    "Heun": heun_values,
    "Eroare Heun": error_heun,
    "RK4": rk4_values,
    "Eroare RK4": error_rk4
})

display(df_compare.round(4))

# Grafic comparativ

r_fine = np.linspace(r0, r_final, 300)
exact_fine = exact(r_fine)

plt.figure(figsize=(10, 6))

plt.plot(r_fine, exact_fine, label="Solutie exacta")
plt.plot(r_values, euler_values, marker="o", linestyle="--", label="Euler")
plt.plot(r_values, heun_values, marker="s", linestyle="--", label="Heun")
plt.plot(r_values, rk4_values, marker="^", linestyle="--", label="Runge-Kutta 4")

plt.title("Compararea solutiei exacte cu metodele Euler, Heun si Runge-Kutta 4")
plt.xlabel("r")
plt.ylabel("P(r)")
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.show()