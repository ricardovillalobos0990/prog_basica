import tkinter as tk
from tkinter import messagebox

def validar():
    if entrada1.get()=="lili":#Get trae lo introducido en la entrada 1 si es igual abre ventana
        abrirventana2()
    else:
        messagebox.showwarning(" Contraseña incorrecta: ")#Si la entrada no es igua que el pass

def abrirventana2():
    ventana.withdraw()#Se cierre al ventana principal
    win=tk.Toplevel()#Top level crea una venta y toma los atributos del padre
    win.geometry("500x420+900+50")#Geometria de la pantalla por lo general es 500x420
    win.configure(bg="dark turquoise")#Fondo de la ventana
    e3 = tk.Label(win, text="Bienvenidos a la segunda ventana ", bg="blue", fg="white")#la etiqueta de la nueva pantalla bg es el fondo de la letra
    e3.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)#pack es la orientacion de la etiqueta
    boton2=tk.Button(win,text="OK", command=win.destroy)#boton se llama ok y llama a la funcion cerrar ventana
    boton2.pack(side=tk.TOP)

def cerrarventana():
    ventana.destroy()

ventana=tk.Tk()#
ventana.title("Ventana Principal ")#Titulo de la ventana principal
ventana.geometry("500x420")#Tamañp
ventana.configure(bg="Red")#Color de fondo

e1=tk.Label(ventana,text=" Ingrese su Password",bg="green",fg="white")#la etiqueta de la nueva pantalla bg es el fondo de la letra
e1.pack(padx=5,pady=5,ipadx=5,ipady=5)#el fondo de la letra
entrada1=tk.Entry(ventana)#
entrada1.pack(padx=10,pady=10,ipadx=2,ipady=2)

boton=tk.Button(ventana,text="Nueva ventana", fg="blue",command=abrirventana2)#Boton que llama a la funcion abrir ventana2
boton.pack(side=tk.TOP)

boton3=tk.Button(ventana,text="Validar Contraseña", fg="blue", command=validar)#Boton que llama a la funcion validar
boton3.pack(side=tk.TOP)#
boton3=tk.Button(ventana,text="OK", command=ventana.destroy)#boton se llama ok y llama a la funcion cerrar ventana
boton3.pack(side=tk.TOP)

ventana.mainloop()