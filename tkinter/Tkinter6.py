import tkinter as tk

ventana = tk.Tk()
ventana.title = ("Formulario")
ventana.geometry("600x500")
ventana.configure(bg="white",)

e1=tk.Label(ventana,text="Nombre:", bg="orange",fg="white")
e1.pack(padx=10,pady=10,ipadx=20,ipady=20,fill=tk.X)
entrada1=tk.Entry(ventana)
entrada1.pack(padx=20,pady=20,ipadx=5,ipady=5,fill=tk.X)

e2=tk.Label(ventana,text="Apellido :", bg="gold",fg="white")
e2.pack(padx=10,pady=10,ipadx=20,ipady=20,fill=tk.X)
entrada2=tk.Entry(ventana)
entrada2.pack(padx=20,pady=20,ipadx=5,ipady=5,fill=tk.X)

e3=tk.Label(ventana,text="Facebook:", bg="purple",fg="white")
e3.pack(padx=10,pady=10,ipadx=20,ipady=20,fill=tk.X)
entrada3=tk.Entry(ventana)
entrada3.pack(padx=20,pady=20,ipadx=5,ipady=5,fill=tk.X)

image=tk.PhotoImage(file="descarga.gif")
image=image.subsample(1,1)
label=tk.Label(image=image)
label.pack()

ventana.mainloop()