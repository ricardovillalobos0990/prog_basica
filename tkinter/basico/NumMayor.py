#DETERMINAR EL NUMERO MAYOR

num1 = int(input("Digite el numero 1: "))
num2 = int(input("Digite el numero 2: "))
num3 = int(input("Digite el numero 3: "))

if num1 > num2 and num1 > num3:
    print(f"{num1} es el mayor ")
elif num2 > num1 and num2 > num3:
    print(f"{num2} es el mayor ")
elif num3 > num1 and num3 > num2:
    print(f"{num3} es el mayor ")
else:
    print("Los numeros son iguales ")