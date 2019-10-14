#!/usr/bin/env python
# coding: utf-8

# In[4]:


from random import choice
from numpy import array, dot, random
import matplotlib.pyplot as plt

class Perceptron:
    def __init__(self, entradas, salidas, bahias, n):
        total = len(entradas)
        entrenamiento = []
        for i in range(total):
            entrenamiento.append(array((array(entradas[i]), salidas[i])))
    
        self.entrenamiento = entrenamiento
        self.w = random.rand(3)
        self.errores = []
        self.esperados = []
        self.bahias = bahias
        self.n = n
    
    
    def activacion(self, x = 0):
        return 0 if x < 0  else 1

    def entrenar(self):
        for i in range(self.n):
            x, esperado = choice(self.entrenamiento)
            resultado = dot(self.w, x)
            self.esperados.append(esperado)
            error = esperado - self.activacion(resultado)
            self.errores.append(error)
            #Ajuste
            self.w += self.bahias * error * x

    def imprimirResultado(self):
        for x, _ in self.entrenamiento:
            resultado = dot(self.w, x)
            print("{}: {} -> {}".format(x[:3], resultado, self.activacion(resultado)))

        plt.title("")
        plt.plot(self.errores,'-',color='red')
        plt.plot(self.esperados,'*', color='green')
        plt.show()