# Modelul revenirii pretului unei actiuni spre valoarea fundamentala

Acest proiect contine implementarea numerica a unui model diferential simplificat pentru revenirea pretului unei actiuni spre valoarea sa fundamentala.

Modelul este realizat pentru materia **Ecuatii Diferentiale si Derivate Partiale** si compara solutia exacta cu trei metode numerice:

- Metoda Euler
- Metoda Heun
- Metoda Runge-Kutta de ordinul 4

## Descrierea modelului

Modelul analizat este:

```math
y'(t) = a(V - y(t)), \quad P(0) = P_0
