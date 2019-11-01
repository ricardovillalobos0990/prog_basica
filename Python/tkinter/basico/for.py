# BUCLE FOR
# inicio = int(input("Indique el numero inicial: "))
# final = int(input("Indique el numero Final: "))
# aumento = int(input("Indique el aumento: "))
# for i in range(inicio, final, aumento):
#     print(f"elemento {i}")(

meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

for i in meses:
    print(f"El Mes es: {i}")


for i,mes in enumerate(meses):
    print(f"El mes # {i+1} es {mes},", end=" ")
print("")
print(meses[::-3])