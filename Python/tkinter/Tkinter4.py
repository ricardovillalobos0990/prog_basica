import tkinter as tk

ventana = tk.Tk()#Ventana principal
ventana.title("Lista despegable")
ventana.geometry("500x420+900+50")#Tamaño o posicion
ventana.configure(bg="green")#Color de fondo

var=tk.StringVar(ventana)
var.set("Rojo")

opciones=["Azul", "Amarillo" , "Verde " , "Morado"]
opcion=tk.OptionMenu(ventana,var,*opciones)
opcion.config(width=20)#Ancho
opcion.pack(side="left",padx=30,pady=30)# Para que este en el lado izquierdo
e1=tk.Label(ventana,text="Color a seleccionar",bg="red",fg="white")
e1.pack(padx=5,pady=5,ipadx=5,ipady=5,fill=tk.X)
color=tk.Label(ventana,bg="plum",textvariable=var,padx=5,pady=5,width=50)
color.pack()
ventana.mainloop()


