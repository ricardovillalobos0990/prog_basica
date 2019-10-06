from tkinter import ttk, messagebox
from tkinter import *
from random import choice
from numpy import array, dot, random
import matplotlib.pyplot as plt


class RedesNeuronales:
    def __init__(self):
        #  initializations

        self.wind = window
        self.wind.title(" Inteligencia Artificial")
        self.wind.geometry("450x200")
        #DENTRO DE LA VENTANA QUE ES = WIND SE AGREGA "add" los Tabs y
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
        self.textEyelash1 = Label( self.eyelash1, text="Indique la Cantidad de Iteracciones")
        self.textEyelash1.grid(row=1, column=0, columnspan=2, sticky=W+E)

        # El boton para indicar la cantidad de N
        self.buttonRedNeuSim = ttk.Button( self.eyelash1, text="LA CANTIDAD DE ITERACCIONES" )
        self.buttonRedNeuSim.grid(row=2, column=0, sticky=W + E )
        # Al lado del Boton el usuario ingresa el valor
        self.EntradaRedNeuSim = Entry(self.eyelash1)
        self.EntradaRedNeuSim.grid(row=2, column=1, sticky=W + E)



        self.pest2 = ttk.Frame(self.eyelash)
        self.eyelash.add( self.pest2, text="Red Neuronal Multiple Capa" )
        self.texto3 = Label( self.pest2, text="Pestaña 2" ).pack()

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

        for x, _ in entrenamiento:
            resultado = dot( w, x )
            print( "{}: {} -> {}".format( x[:3], resultado, activacion( resultado ) ) )
            self.message['text'] = f"{x[:3]}: {resultado} -> {activacion( resultado )}"
            self.message.grid( row=3, column=0, columnspan=2, sticky=W + E )

        plt.plot( errores, '-', color='red' )
        plt.plot( esperados, '*', color='green' )
        #plt.legend()
        plt.title("RED PERCEPTRON")
        plt.xlabel( 'Eje: X' )
        plt.ylabel( 'Eje: Y' )
        plt.grid()
        plt.show()


class RedNeuronalSimple(RedesNeuronales):
    clave = RedesNeuronales()
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

    def showRedNeuronalSimple(self):
        entradas = array( [[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]] )
        salidas = array( [[0, 1, 1, 0]] ).T
        print(self.pesos_signaticos)
        #entrenamiento(entradas, salidas, 1000)
        #print( self.pesos_signaticos )
        #print( self.pensar( array( [1, 0, 0] ) ) )


if __name__ == "__main__":
    window = Tk()
    application = RedesNeuronales()
    application.wind
    window.mainloop()