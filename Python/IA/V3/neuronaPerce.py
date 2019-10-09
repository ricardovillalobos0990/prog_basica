from tkinter import ttk
from tkinter import *
from random import choice
from numpy import  array, dot, random
import numpy as np
import matplotlib.pyplot as plt
from neuronaSim import RedNeuronalSimple
from neuronaMul import RedNeuronalMultiple


class Perceptron(RedNeuronalSimple, RedNeuronalMultiple):

    def __init__(self, window):
        #  initialization
        self.pesos_signaticos = 2 * random.random( (3, 1) ) - 1

        self.wind = window
        self.wind.title(" Inteligencia Artificial")
        self.wind.geometry("450x200")
        self.eyelash = ttk.Notebook(self.wind)
        self.eyelash.pack(fill='both',expand='yes')

        # Se crea la pestasña Perceptron
        self.eyelash0 = ttk.Frame(self.eyelash)
        self.eyelash.add(self.eyelash0,text="Perceptron")
        textEyelash0 = Label(self.eyelash0,text="Ingrese el Valor para N para el Perceptron")
        textEyelash0.grid(row=1, column=0, columnspan=2, sticky=W+E)
        buttonPer = ttk.Button(self.eyelash0, text="LA CANTIDAD DE N", command=self.validacionPerceptron)
        buttonPer.grid(row=2, column=0, sticky=W + E )
        self.perEntradaN = Entry(self.eyelash0)
        self.perEntradaN.grid(row=2, column=1, sticky=W + E)

        # Se crea la pestasña Red Neuronal Simple
        self.eyelash1 = ttk.Frame(self.eyelash)
        self.eyelash.add( self.eyelash1, text="Red Neuronal Simple" )
        textEyelash1 = Label( self.eyelash1, text="Indique la Cantidad de Iteracciones")
        textEyelash1.grid(row=1, column=0, columnspan=2, sticky=W+E)
        buttonRedNeuSimple = ttk.Button( self.eyelash1, text="LA CANTIDAD DE ITERACCIONES", command=self.showSimple)
        buttonRedNeuSimple.grid(row=2, column=0, sticky=W + E )
        self.entradaRedNeuSimple = Entry(self.eyelash1)
        self.entradaRedNeuSimple.grid(row=2, column=1, sticky=W + E)

        # Se crea la pestasña Red Neuronal Multiple
        self.eyelash2 = ttk.Frame(self.eyelash)
        self.eyelash.add(self.eyelash2, text="Red Neuronal Multiple" )
        textEyelash2 = Label(self.eyelash2, text="Indique la Cantidad de ALgo")
        textEyelash2.grid(row=1, column=0, columnspan=2, sticky=W+E)
        buttonRedNeuMul = ttk.Button( self.eyelash2, text="LA CANTIDAD DE ALGO", command=self.showMultiple)
        buttonRedNeuMul.grid(row=2, column=0, sticky=W + E )
        self.entradaRedNeuMul = Entry(self.eyelash2)
        self.entradaRedNeuMul.grid(row=2, column=1, sticky=W + E)

        # Output Messages
        self.message = Label( self.eyelash0, text='', fg='red' )
        self.message.grid( row=5, column=0, columnspan=2, sticky=W + E )

    def validacionPerceptron(self):
        if int(self.perEntradaN.get()) > 0:
            self.perceptron()
        else:
            self.message["text"] =  f" Eligio el # {self.perEntradaN.get()} El Numero Introducido debe ser MAYOR a 0"

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
        for i in range (int(self.perEntradaN.get())):
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
        #plt.legend()
        plt.title("RED PERCEPTRON")
        plt.xlabel( 'Eje: X' )
        plt.ylabel( 'Eje: Y' )
        plt.grid()
        plt.show()


    def showSimple(self):
        entradas = array( [[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]] )
        salidas = array( [[0, 1, 1, 0]] ).T
        self.entrenamiento( entradas, salidas, 1000)
        print( self.pesos_signaticos )
        print( self.pensar( array( [1, 0, 0] ) ) )

    def showMultiple(self):
        nn = RedNeuronalMultiple( [2, 3, 2], activacion='tangente' )

        X = np.array( [[0, 0],  # sin obstaculos
                       [0, 1],  # sin obstaculos
                       [0, -1],  # sin obstaculos
                       [0.5, 1],  # obstaculo detectado a la derecha
                       [0.5, -1],  # obstaculo a izquierdad
                       [1, 1],  # demasiado cerca a la derecha
                       [1, -1]] )  # demasiado cerca a la izquierda

        y = np.array( [[0, 1],  # avanzar
                       [0, 1],  # avanzar
                       [0, 1],  # avanzar
                       [-1, 1],  # giro izquierda
                       [1, 1],  # giro derecha
                       [0, -1],  # retroceder
                       [0, -1], ] )  # retroceder

        nn.ajuste( X, y, factor_aprendizaje=0.03, epocas= int(self.entradaRedNeuMul.get()))

        index = 0
        for e in X:
            print( "X: ", e, "y: ", y[index], "Red: ", nn.predecir( e ) )
            index = index + 1

        import matplotlib.pyplot as plt
        """%matplotlib inline"""
        deltas = nn.obtener_deltas()
        valores = []
        index = 0
        for arreglo in deltas:
            valores.append( arreglo[1][0] + arreglo[1][1] )
            index = index + 1

        plt.plot( range( len( valores ) ), valores, color='b' )
        plt.ylim( [0, 1] )
        plt.ylabel( 'Costo' )
        plt.xlabel( 'Epocas' )
        plt.title("Red Neuronal Multiple")
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    window = Tk()
    application = Perceptron(window)
    window.mainloop()