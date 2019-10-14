from tkinter import ttk
from tkinter import *
from Perceptron import Perceptron
from RedNeuronalSimple import RedNeuronalSimple
from RedNeuronalMulticapa import RedNeuronalMulticapa
from numpy import array, dot, random

class RedesNeuronales:

    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Hola Mundo")
        self.ventana.geometry("600x500")
        self.notebook = ttk.Notebook(self.ventana)
        self.notebook.pack(fill='both',expand='yes')
        self.entradas = {}
        self.salidas = {}
        self.bahias = {}
        self.activacion = {}
        self.entrenamiento = {}
        self.instances = {}
        self.ob = {}
    
    def createFrame(self, instancia, title):
        self.instances[instancia] = ttk.Frame(self.notebook)
        self.notebook.add( self.instances.get(instancia), text=title)

    def interface(self, instancia, Ob):
        etiquetaEntradas = []
        etiquetaSalidas = []
        nombreEntradas = []
        nombreSalidas = []
        self.entradas[instancia] = []
        self.salidas[instancia] = []

        etiquetaEntradas.append(Label(self.instances.get(instancia),text="Ingrese la misma cantidad de item para cada entrada, separados por coma y sin espacio. ").place(x=10 ,y=0))
        i = 0
        for i in range(4):
            etiquetaEntradas.append(Label(self.instances.get(instancia),text="Entrada # " + str(i) + ' :').place(x=10 ,y=50 + i * 20))
            self.entradas[instancia].append(StringVar())
            nombreEntradas.append(Entry(self.instances.get(instancia), textvariable=self.entradas[instancia][i]).place(x=110,y=50+ i * 20))

            self.salidas[instancia].append(StringVar())
            etiquetaSalidas.append(Label(self.instances.get(instancia),text="Salida # " + str(i) + ' :').place(x=300 ,y=50 + i * 20))
            nombreSalidas.append(Entry(self.instances.get(instancia), textvariable=self.salidas[instancia][i]).place(x=380,y=50 + i * 20))

        etiquetaBahias = Label(self.instances.get(instancia),text="Ingrese el sesgo de bahias").place(x=10 ,y=50 + (i+2) * 20)
        self.bahias[instancia] = DoubleVar()
        nombreBahias = Entry(self.instances.get(instancia),textvariable=self.bahias[instancia]).place(x=180,y=50 + (i+2) * 20)

        etiquetaEntrenamiento = Label(self.instances.get(instancia),text="Ingrese entrenamiento").place(x=10 ,y=50 + (i+3) * 20)
        self.entrenamiento[instancia] = IntVar()
        nombreEntrenamiento = Entry(self.instances.get(instancia),textvariable=self.entrenamiento[instancia]).place(x=180,y=50 + (i+3) * 20)

        self.activacion[instancia] = StringVar()
        opciones = ttk.Combobox(self.instances.get(instancia),values=("Sigmoide","Tangente"),textvariable=self.activacion[instancia]).place(x=10, y=50 + (i+5) * 20)

        self.ob[instancia] = Ob
        boton1 = Button(self.instances.get(instancia),text="Entrenar",fg="green", command=lambda: self.callNeurona(instancia)).pack(padx=30, pady=50 + (i+6) * 20)
    
    def callNeurona(self, instancia):
        total = len(self.entradas[instancia])
        entradas = []
        salidas = []

        for i in range(total):
            entradas.append([int(x) for x in self.entradas[instancia][i].get().split(sep=',')])
            salida  = [int(x) for x in self.salidas[instancia][i].get().split(sep=',')]
            if len(salida) == 1: 
                salidas.append(int(salida[0])) 
            else:
                 salidas.append(salida)

        ob = self.ob[instancia](entradas, salidas, self.bahias[instancia].get(), self.entrenamiento[instancia].get())
        ob.entrenar()
        ob.imprimirResultado()



            

            
        # nombreEntrada = Entry(ventana,textvariable=nombre).place(x=110,y=10)

        # etiqueta = Label(ventana,text="Ingrese Nombre: ").place(x=10,y=10)
        # nombreEntrada = Entry(ventana,textvariable=nombre).place(x=110,y=10)

        # etiqueta = Label(ventana,text="Ingrese Nombre: ").place(x=10,y=10)
        # nombreEntrada = Entry(ventana,textvariable=nombre).place(x=110,y=10)

        # etiqueta = Label(ventana,text="Ingrese Nombre: ").place(x=10,y=10)
        # nombreEntrada = Entry(ventana,textvariable=nombre).place(x=110,y=10)
        
    def sostenerVentana(self):
        self.ventana.mainloop()
    

ob = RedesNeuronales()
ob.createFrame('red', 'Perceptrón')
ob.createFrame('red2', 'Red neuronal simple')
ob.createFrame('red3', 'Red neuronal multicapa')
ob.interface('red', Perceptron)
ob.interface('red2', RedNeuronalSimple)
ob.interface('red3', RedNeuronalMulticapa)
ob.sostenerVentana()