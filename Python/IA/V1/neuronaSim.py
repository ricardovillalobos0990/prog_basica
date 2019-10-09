from random import choice
from numpy import exp, array, dot, random
#import neuronaPerce

class RedNeuronalSimple():

    def __init__(self):
        self.pesos_signaticos = 2 * random.random((3, 1)) - 1
        
    def __sigmoide(self, x):
        return 1 / (1 + exp(-x))

    def __sigmoide_derivado(self, x):
        return x * (1 - x)

    def entrenamiento(self, entradas, salidas, numero_iteraciones):
        for i in range(numero_iteraciones):
            salida = self.pensar(entradas)
            error = salidas - salida
            ajuste = dot(entradas.T, error * self.__sigmoide_derivado(salida))
            self.pesos_signaticos += ajuste

    def pensar(self, entradas):
        return self.__sigmoide(dot(entradas, self.pesos_signaticos))

    
    def showRedSimple(self):
        entradas = array( [[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]] )
        salidas = array( [[0, 1, 1, 0]] ).T
        self.entrenamiento( entradas, salidas, 1000 )
        print( self.pesos_signaticos )
        print( self .pensar( array( [1, 0, 0] ) ) )
        #clave = neuronaPerce.Perceptron()
        #neuronaPerce.Perceptron.message["text"] = "Hola"
        #Perceptron.message["text"]="HOLA"