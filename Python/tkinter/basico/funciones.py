def edad(nombre, nacimiento):
    nombre = nombre.upper()
    edad = 2019-nacimiento
    print(f"{nombre} tiene {edad} años")

nombre = input("Digite su nombre: ")
nac = int(input("Digite la fecha de nacimiento "))
edad(nombre, nac)

def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def mult(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

def mostrar_resultado(x):
    print(x(6,20))

operacion = mult
mostrar_resultado(operacion)

def letra(valor):
    return valor.isalpha()
cadena = input("Digite la cadena: ")
while letra(cadena)==False:
    print("Digite nuevamente la cadena :")
    cadena = input("Digite la cadena: ")
print(f" Es correcto el nombre : {cadena}")