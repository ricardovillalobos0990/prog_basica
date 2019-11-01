import tkinter as tk
from tkinter import Tk

def suma(*args):
    suma=int(entrada1.get())+ int(entrada2.get())
    return var.set(suma)

def cerrar():
    ventana.destroy()

ventana: Tk = tk.Tk()
ventana.title("Ventana de la Operacion Suma")
ventana.geometry("500x420")
ventana.configure(background="blue")

var=tk.StringVar()

e1 = tk.Label(ventana, text=' Numero1', bg="red", fg="white")
e1.pack(padx=20, pady=20, ipadx=20, ipady=20, fill=tk.X)
entrada1 = tk.Entry(ventana)
entrada1.pack(fill=tk.X,padx=5,pady=5,ipadx=5,ipady=5)

e2 = tk.Label(ventana, text=' Numero 2', bg="red", fg="white")
e2.pack(padx=20, pady=20, ipadx=20, ipady=20, fill=tk.X)
entrada2 = tk.Entry(ventana)
entrada2.pack(fill=tk.X,padx=5,pady=5,ipadx=5,ipady=5)

botonsuma=tk.Button(ventana,text="Suma",fg="blue",command=suma)
botonsuma.pack(side=tk.TOP)

res=tk.Label(ventana,bg="red",textvariable=var,padx=5,pady=5,width=50)
res.pack()

botonsuma=tk.Button(ventana,text="Cerrar",fg="blue",command=cerrar)
botonsuma.pack(side=tk.TOP)

ventana.mainloop()
