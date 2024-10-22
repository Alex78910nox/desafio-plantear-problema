import numpy as np
import matplotlib.pyplot as plt

# Datos originales
anios = np.array([2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022])
produccion = np.array([45.0, 39.5, 39.1, 38.6, 38.6, 36.4, 34.6, 33.0, 39.0, 36.3, 35.0])

# Interpolación de Newton
def diferencias_divididas(x, y):
    n = len(y)
    coef = np.copy(y)
    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            coef[i] = (coef[i] - coef[i-1]) / (x[i] - x[i-j])
    return coef

def polinomio_newton(x_data, coef, x):
    n = len(coef) - 1
    p = coef[n]
    for k in range(1, n+1):
        p = coef[n-k] + (x - x_data[n-k]) * p
    return p

coef_newton = diferencias_divididas(anios, produccion)

# Interpolación de Lagrange
def lagrange(x_data, y_data, x):
    n = len(x_data)
    p = 0
    for i in range(n):
        L = 1
        for j in range(n):
            if i != j:
                L *= (x - x_data[j]) / (x_data[i] - x_data[j])
        p += y_data[i] * L
    return p

# Gráfica de resultados
x_nuevos = np.linspace(2012, 2022, 100)
y_newton = [polinomio_newton(anios, coef_newton, xi) for xi in x_nuevos]
y_lagrange = [lagrange(anios, produccion, xi) for xi in x_nuevos]

# Graficar
plt.plot(anios, produccion, 'o', label="Datos reales")
plt.plot(x_nuevos, y_newton, '-', label="Interpolación Newton")
plt.plot(x_nuevos, y_lagrange, '--', label="Interpolación Lagrange")
plt.xlabel("Año")
plt.ylabel("Producción (miles de toneladas)")
plt.legend()
plt.title("Interpolación de la producción agrícola en Bolivia")
plt.grid(True)
plt.show()

# Comparación en el año 2017-2018
anio_comparacion = 2023
real = 35  # Valor corregido del gráfico
newton_valor = polinomio_newton(anios, coef_newton, anio_comparacion)
lagrange_valor = lagrange(anios, produccion, anio_comparacion)

print(f"Valor interpolado con Newton en {anio_comparacion}: {newton_valor:.2f}")
print(f"Valor interpolado con Lagrange en {anio_comparacion}: {lagrange_valor:.2f}")
print(f"Valor real en {anio_comparacion}: {real}")
