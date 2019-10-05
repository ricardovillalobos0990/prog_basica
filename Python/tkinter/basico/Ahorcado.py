import time
nombre=input("Cual es su nombre? ")
print(f"Hola {nombre} Es hora de Jugar al Ahorcado ")
print("")
time.sleep(2)
print("Comienza a JUGAR ")
time.sleep(0.5)
palabra="ricardito"
tupalabra=""
vidas=5

while vidas > 0:
    fallas=0
    for letra in palabra:
        if letra in tupalabra:
            print(letra, end="")
        else:
            print("*", end="")
            fallas+=1
    if fallas==0:
        print("Feliciades Ganaste ")
        break

    tuletra=input(" Introduce una Letra")
    tupalabra+=tuletra

    if tuletra not  in palabra:
        vidas-=1
        print(" Equivocacion ")
        print(f"Tu tienes {vidas} vidas")

    if vidas == 0:
        print("Perdiste")
else:
        print("Gracias por participar")
