import tkinter as tk

ventana = tk.Tk()
ventana.title("Hola Mundo")
#ANCHO X ALTO
ventana.geometry('500x420')
ventana.configure(background='dark turquoise')
etiqueta1 = tk.Label(ventana,text=" Bienvenidos", bg="red", fg="white")
etiqueta1.pack(padx=20,pady=20,side=tk.LEFT)

etiqueta2 = tk.Label(ventana, text=" A la ventana", bg="pink", fg="white")
#etiqueta2.pack(padx=20,pady=20)
etiqueta2.pack(padx=20,pady=20,side=tk.LEFT)

etiqueta3 = tk.Label(ventana,text=" The Pitbulls", bg="gold", fg="black")
etiqueta3.pack(padx=20,pady=20,side=tk.LEFT)

ventana.mainloop()