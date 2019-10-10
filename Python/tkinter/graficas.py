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

        Label(self.wind, text="VAMOS A REALIZAR OPERACIONES").grid(row=0, column=0, columnspan=2)
        button = Button(self.wind, text="Ingrese el Numero para la SUMA")
        button.grid(row=1, column=0)
        self.entryMain = Entry(self.wind, textvariable=self.valor1)
        self.entryMain.grid(row=1, column=1)
        button = Button( self.wind, text="Ingrese el Numero para la SUMA", command=self.validar)
        button.grid( row=2, column=0, columnspan=1 )
        self.entryMain = Entry( self.wind, textvariable=self.valor2)
        self.entryMain.grid( row=2, column=1 )

    def validar(self):
        if 2 > 0:
            Operaciones.suma(self, int(self.valor1.get()), int(self.valor2.get()))
            self.valor1.set()

if __name__ == "__main__":
    window = Tk()
    aplication = MainWindow(window)
    window.mainloop()