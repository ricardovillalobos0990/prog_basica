#Condicionales Combinados

edad = int(input("Digite su edad: "))

if edad>0 and edad<100:
    print("La edad es correcta ")
    if edad>=18:
        print("Es mayor de edad ")
else:
    print("Edad incorrecta ")