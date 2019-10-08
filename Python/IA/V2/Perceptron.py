#from Red import Red
from tkinter import *
from random import choice
from numpy import exp, array, dot, random
import matplotlib.pyplot as plt


class Perceptron:
    def __init__(self):
        super().__init__(window="")

    def validacionPerceptron(self):
        if int( 10  ) > 0:
            self.perceptron()
        else:
            self.message["text"] = f" Eligio el #  El Numero Introducido debe ser MAYOR a 0"
""""
    def perceptron(self):
        # Funcion de Activación
        activacion = lambda x: 0 if x < 0 else 1
        # Set de Entrenamiento
        entrenamiento = [
            (array( [0, 0, 1] ), 0),
            (array( [0, 1, 1] ), 1),
            (array( [1, 0, 1] ), 1),
            (array( [1, 1, 1] ), 1),
        ]

        w = random.rand( 3 )
        errores = []
        esperados = []
        bahias = 0.2

        # Entrenamiento
        for i in range( int( self.perEntradaN.get() ) ):
            x, esperado = choice( entrenamiento )
            resultado = dot( w, x )
            esperados.append( esperado )
            error = esperado - activacion( resultado )
            errores.append( error )
            # Ajuste
            w += bahias * error * x

        cadena0 = ''
        for x, _ in entrenamiento:
            resultado = dot( w, x )
            cadena0 += f"{x[:3]}: {resultado} -> {activacion( resultado )} \n"
        self.message['text'] = cadena0
        self.message.grid( row=3, column=0, columnspan=2, sticky=W + E )

        plt.plot( errores, '-', color='red' )
        plt.plot( esperados, '*', color='green' )
        # plt.legend()
        plt.title( "RED PERCEPTRON" )
        plt.xlabel( 'Eje: X' )
        plt.ylabel( 'Eje: Y' )
        plt.grid()
        plt.show()"""