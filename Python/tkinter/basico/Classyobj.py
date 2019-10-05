class Lapiz:
    color = "Amarillo"
    contiene_borrador = True
    usa_grafito = True

    def dibujar(self):
        if self.condicion():
            print("Dibuja y borra")
        else:
            print(" Solo dibuja")

    def borrar(self):
        print("Borra")

    def condicion(self):
        return self.contiene_borrador

#Esto es un objeto
lapiz_generico = Lapiz()
lapiz_generico.dibujar()


