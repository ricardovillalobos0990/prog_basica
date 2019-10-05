from random import choice
from numpy import array, dot, random
import matplotlib.pyplot as plt

#FUNCION DE ACTIVACION
activacion = lambda x:0 if x < 0 else 1

#SET DE ENTRENAMIENTO
entrenamiento = [
    (array([0, 0, 1]), 0),
    (array([0, 1, 1]), 1),
    (array([1, 0, 1]), 1),
    (array([1, 1, 1]), 1),
]

w = random.rand(3)
errores = []
bahias = 0.2
n = 20

#ENTRENAMIENTO
for i in range(n):
    x, esperado = choice(entrenamiento)
    resultado = dot(w, x)
    esperados.append(esperado)
    error = esperado - activacion(resultado)
    errores.append(error)
    # AJUSTE
    w += bahias * error * x

for x, _ in entrenamiento:
    resultado = dot (w, x)
    print("{}: {} -> {}".format(x[:3], resultado, activacion(resultado)))

plt.plot(errores)
plt.plot(esperados)