class lapiz():
    def __init__(self, color, contiene_borrador, usa_grafito):
        self.color = color
        self.contiene_borrador = contiene_borrador
        self.usa_grafito = usa_grafito
    
    #Metodos
    def dibujar(self):
        print ("El lapiz esta dibujando")
        return  


    def borrar(self):
        if self.es_valido_para_borrar():
            print("El lapiz esta borrando")
        else:
            print("El lapiz no esta borrando")
        return

    def es_valido_para_borrar(self):
        return self.contiene_borrador

lapiz_generico = lapiz("Verde" , True, True) # Se instancia la clase Lapiz en el Objeto Lapiz Generico
lapiz_generico.contiene_borrador = True
lapiz_generico.dibujar()
lapiz_generico.borrar()