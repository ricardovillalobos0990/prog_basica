from tkinter import ttk, messagebox
from tkinter import *
from Operaciones import Operaciones

class MainWindow(Operaciones):
    def __init__(self, window):
        self.wind = window
        self.wind.title("Grafica")
        self.wind.geometry("500x400")
        self.valor1 = IntVar()
        self.valor2 = IntVar()
        self.resultado = IntVar()

        #SUMA
        self.eyelash = ttk.Notebook(self.wind)
        self.eyelash.pack(fill='both',expand='yes')
        self.eyelash0 = ttk.Frame( self.eyelash )
        self.eyelash.add( self.eyelash0, text="SUMA" )
        Label(self.eyelash0, text="USE LAS CASILLAS" ).grid( row=0, column=0, columnspan=2, sticky=W + E )
        Label(self.eyelash0, text="Numero 1").grid(row=1, column=0)
        self.entrySum = Entry(self.eyelash0, textvariable=self.valor1)
        self.entrySum.grid(row=1, column=1)
        Label(self.eyelash0, text="Numero 2").grid( row=2, column=0, columnspan=1 )
        self.entrySum = Entry( self.eyelash0, textvariable=self.valor2)
        self.entrySum.grid( row=2, column=1 )
        button = Button(self.eyelash0, text="SUMA", command=self.validarSum)
        button.grid(row=3, column=0)
        self.message = Label(self.eyelash0, textvariable=self.resultado, fg='red')
        self.message.grid( row=3, column=1, columnspan=2, sticky=W + E )

        self.eyelash1 = ttk.Frame( self.eyelash )
        self.eyelash.add( self.eyelash1, text="RESTA" )
        Label( self.eyelash1, text="USE LAS DOS CASILLAS" ).grid( row=0, column=0, columnspan=2, sticky=W + E )
        Label( self.eyelash1, text="Numero 1" ).grid( row=1, column=0 )
        self.entryRes = Entry( self.eyelash1, textvariable=self.valor1 )
        self.entryRes.grid( row=1, column=1 )
        Label( self.eyelash1, text="Numero 2" ).grid( row=2, column=0, columnspan=1 )
        self.entryRes = Entry( self.eyelash1, textvariable=self.valor2 )
        self.entryRes.grid( row=2, column=1 )
        button = Button( self.eyelash1, text="RESTA", command=self.validarRes)
        button.grid( row=3, column=0 )
        self.message = Label( self.eyelash1, textvariable=self.resultado, fg='red' )
        self.message.grid( row=3, column=1, columnspan=2, sticky=W + E )

    def validarSum(self):
        if 10 > 0:
            Operaciones.suma(self, int(self.valor1.get()), int(self.valor2.get()))
            self.res.set(self.sum)

    def validarRes(self):
        if 10 > 0:
            Operaciones.resta(self, int(self.valor1.get()), int(self.valor2.get()))
            self.resultado.set(self.res)


if __name__ == "__main__":
    window = Tk()
    aplication = MainWindow(window)
    window.mainloop()