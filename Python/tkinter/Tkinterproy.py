from tkinter import ttk, messagebox
from tkinter import *

class Menu:
    def __init__(self, window):
        #  initializations

        self.wind = window
        self.wind.title(' Menu Opciones ')
        self.valor = IntVar()

        # Create a frame Container
        frame = LabelFrame(self.wind, text=" Opciones ")
        frame.grid(row=0, column=0, columnspan=5, pady=5)

        # Name Input
        Label(frame, text="1# Sum ").grid(row=1, column=0)
        Label(frame, text="2# Res ").grid(row=1, column=1)
        Label(frame, text="3# Mul ").grid(row=1, column=2)
        Label(frame, text="4# Div ").grid(row=1, column=3)
        Label(frame, text="5# Exp ").grid(row=1, column=4)
        # Opcion Input
        Label(frame, text=" Entry Option ").grid(row=2, column=0)
        self.opcion = Entry(frame)
        self.opcion.focus()
        self.opcion.grid(row=2, column=1)

        # Buttons
        ttk.Button(frame, text="Confirm ", command=self.validar).grid(row=2, column=2, columnspan=3, sticky=W + E)

        # Output Messages
        self.message = Label(text='', fg='red')
        self.message.grid(row=3, column=0, columnspan=2, sticky=W + E)

    def validar(self):
        if self.opcion.get() == "1":
            self.window_suma()
        elif self.opcion.get() == "2":
            self.window_res()
        else:
            messagebox.showwarning("Contraseña incorrecta: ")  # Si la entrada no es igua que el pass

    def window_suma(self):
        self.edit_wind = Toplevel()
        self.edit_wind.title = ('SUMA')
        self.valor = IntVar()
        # Old Name
        Label(self.edit_wind, text="Operacion suma ").grid(row=0, column=1, sticky=W + E)
        # New Name
        Label(self.edit_wind, text=" Digite el numero 1").grid(row=1, column=1)
        self.num1 = Entry(self.edit_wind)
        self.num1.grid(row=1, column=2)
        Label(self.edit_wind, text=" Digite el numero 2").grid(row=2, column=1)
        self.num2 = Entry(self.edit_wind)
        self.num2.grid(row=2, column=2)

        ttk.Button(self.edit_wind, text="Resultado ", command=self.suma).grid(row=3, column=1, sticky=W+E)
        Entry(self.edit_wind, textvariable=self.valor).grid(row=3, column=2)

    def window_res(self):
        self.edit_wind = Toplevel()
        self.edit_wind.title = ('RESTA')
        # Old Name
        self.valor = IntVar()
        Label( self.edit_wind, text="Operacion Resta" ).grid( row=0, column=1, sticky=W+E)
        # New Name
        Label(self.edit_wind, text="Numero 1 ").grid( row=1, column=1)
        self.num1 = Entry(self.edit_wind)
        self.num1.grid(row=1, column=2)
        Label(self.edit_wind, text="Numero 2" ).grid( row=2, column=1)
        self.num2 = Entry(self.edit_wind)
        self.num2.grid(row=2, column=2)

        ttk.Button(self.edit_wind, text="Resultado ", command=self.res).grid(row=3, column=1, sticky=W+E)
        Entry( self.edit_wind, textvariable=self.valor ).grid( row=3, column=2 )

    def suma(self):
        suma = int(self.num1.get()) + int(self.num2.get())
        return self.valor.set(suma)

    def res(self):
        res = int(self.num1.get()) - int(self.num2.get())
        return self.valor.set(res)


if __name__ == "__main__":
    window = Tk()
    application = Menu(window)
    window.mainloop()