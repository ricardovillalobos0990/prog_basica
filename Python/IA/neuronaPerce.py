from tkinter import ttk, messagebox
from tkinter import *
from random import choice
from numpy import exp, array, dot, random
import matplotlib.pyplot as plt
import neuronaSim
import neuronaMul

class Perceptron():
    def __init__(self, window):
        #  initialization
        #simple = clave.RedNeuronalSimple()
        simple = neuronaSim.RedNeuronalSimple()
        multi = neuronaMul.RedNeuronalMultiple()
        
        self.wind = window
        self.wind.title(" Inteligencia Artificial")
        self.wind.geometry("450x200")
        # Dentro de self.wind se agrega llama a la funcion Notebook la cual se guarda en pestaña "eyelash"
        self.eyelash = ttk.Notebook(self.wind)
        self.eyelash.pack(fill='both',expand='yes')


        # Se crea la pestasña Perceptron
        self.eyelash0 = ttk.Frame(self.eyelash)
        self.eyelash.add(self.eyelash0,text="Perceptron")
        # La etiqueta va dentro de pestala para que se ingrese el valor
        self.textEyelash0 = Label(self.eyelash0,text="Ingrese el Valor para N para el Perceptron")
        self.textEyelash0.grid(row=1, column=0, columnspan=2, sticky=W+E)
        # El boton para indicar la cantidad de N
        self.buttonPer = ttk.Button(self.eyelash0, text="LA CANTIDAD DE N", command=self.validacionPerceptron)
        self.buttonPer.grid(row=2, column=0, sticky=W + E )
        #Al lado del Boton el usuario ingresa el valor
        self.perEntradaN = Entry(self.eyelash0)
        self.perEntradaN.grid(row=2, column=1, sticky=W + E)


        # Se crea la pestasña Red Neuronal Simple
        self.eyelash1 = ttk.Frame(self.eyelash)
        self.eyelash.add( self.eyelash1, text="Red Neuronal Simple" )
        # La etiqueta va dentro de pestaña para que se ingrese el valor
        self.textEyelash1 = Label( self.eyelash1, text="Indique la Cantidad de Iteracciones")
        self.textEyelash1.grid(row=1, column=0, columnspan=2, sticky=W+E)
        # El boton para indicar la cantidad de Iteracciones
        self.buttonRedNeuSimple = ttk.Button( self.eyelash1, text="LA CANTIDAD DE ITERACCIONES", command=simple.showRedSimple)
        self.buttonRedNeuSimple.grid(row=2, column=0, sticky=W + E )
        # Al lado del Boton el usuario ingresa el valor
        self.EntradaRedNeuSimple = Entry(self.eyelash1)
        self.EntradaRedNeuSimple.grid(row=2, column=1, sticky=W + E)

        multi.
        # Se crea la pestasña Red Neuronal Multiple
        self.eyelash2 = ttk.Frame(self.eyelash)
        self.eyelash.add(self.eyelash2, text="Red Neuronal Multiple" )
        self.textEyelash2 = Label(self.eyelash2, text="Indique la Cantidad de ALgo")
        self.textEyelash2.grid(row=1, column=0, columnspan=2, sticky=W+E)
        # El boton para indicar la cantidad de No se que
        self.buttonRedNeuMul = ttk.Button( self.eyelash2, text="LA CANTIDAD DE ALGO")
        self.buttonRedNeuMul.grid(row=2, column=0, sticky=W + E )
        # Al lado del Boton el usuario ingresa el valor
        self.EntradaRedNeuMul = Entry(self.eyelash2)
        self.EntradaRedNeuMul.grid(row=2, column=1, sticky=W + E)


        # Output Messages
        self.message = Label( self.eyelash0, text='', fg='red' )
        self.message.grid( row=10, column=0, columnspan=2, sticky=W + E )

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


if __name__ == "__main__":
    window = Tk()
    application = Perceptron(window)
    window.mainloop()