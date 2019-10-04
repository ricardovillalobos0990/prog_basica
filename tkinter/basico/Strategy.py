class Button:
    """A very basic button widget."""
    def __init__(self, submit_func, label):
        self.on_submit = submit_func   # Poner la funcion estrategia directamente
        self.label = label

# Se crean dos objetos con estrategias diferentes
button1 = Button(sum, "Add 'em")
button2 = Button(lambda nums: " ".join(map(str, nums)), "Join 'em")

# Probamos cada boton
numbers = range(1, 10) # Lista del 1 al 9
print (button1.on_submit(numbers)) # muestra "45"
print (button2.on_submit(numbers)) # muestra "1 2 3 4 5 6 7 8 9"