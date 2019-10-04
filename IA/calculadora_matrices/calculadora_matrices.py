import numpy as np
import os

class Calculadora:
    def limparPantalla(self):
        if os.name == "posix":
            os.system ("clear")
        elif os.name == "ce" or os.name == "nt" or os.name == "dos":
            os.system ("cls")

    def showMenu(self):
        self.limparPantalla()
        print ("    ***** MENU *****")
        print ("")
        print ("[1] Suma de Matrices")
        print ("[2] Resta de Matrices")
        print ("[3] Multiplicacion de Matrices")
        print ("[4] Determinante de Matriz")
        print ("[5] Transpuesta de una Matriz")
        print ("[6] Multiplicacion por escalar")
        print ("[7] Generar matriz aleatoria")
        print ("[0] Salir")
        print ("")

    def ingresarMatriz(self, indicativo):
        filas = input(f"Ingrese la cantidad de filas para la matriz {indicativo}: ")
        columnas = input(f"Ingrese la cantidad de columnas para la matriz {indicativo}: ")
        fila = []
        matriz = []
        for f in list(range(int(filas))):
            for c in list(range(int(columnas))):
                fila.append(int(input(f"Elemento [{f}, {c}]: ")))
            matriz.append(fila.copy())
            fila.clear()
        return matriz
    
    def showResult(self, result):
        self.limparPantalla()
        print('')
        print('--------------------')
        print('Matriz resultante:')
        print('')
        print(result)
        print('')
        print('--------------------')
        print('')
        guardar = input('¿ Desea guardar el resultado N/Y ? ')
        if guardar.upper() != 'N':
            self.guardarResultado(result)

    def validarMatricesIguales(self, matrizA, matrizB):
        return all(len(lst) == len(matrizA) for lst in [matrizB])

    def validarMatricesMultiplicacion(self, matrizA, matrizB):

        return len(matrizA[0]) == len(matrizB)

    def sumarMatriz(self, matrizA, matrizB):
        return matrizA  +  matrizB

    def restarMatriz(self, matrizA, matrizB):
        return matrizA  -  matrizB

    def multiplicarMatriz(self, matrizA, matrizB):
        return np.dot(matrizA, matrizB)

    def determinanteMatriz(self, matriz):
        return np.linalg.det(matriz)

    def transponerMatriz(self, matriz):
        return np.transpose(matriz)
    
    def multiplicarEscalarMatriz(self, matriz, escalar):
        return matriz * escalar

    def generarMatrizAleatoria(self):
        filas = int(input("Ingrese el numero de filas: "))
        columnas = int(input("Ingrese el numero de columnas: "))
        result = np.random.randint(-100, 100,(filas, columnas)) 
        self.showResult(result)

    def guardarResultado(self, result):
        dname = 'resultados/'
        fname = []
        for f in os.listdir(dname):
            fname.append(f)
        if len(fname) == 0:
            nuevo = 'file_0'
        else:
            nuevo = 'file_' + str(int(fname[-1].replace('.txt','')[-1])+1)
        
        np.savetxt(dname + nuevo + '.txt', result, delimiter=", ", fmt='%d')
            

    def main(self):
        opcion = 1
        msgerror = "ERROR: Las matrices deben poseer las mismas dimensiones, es decir  la misma cantidad tanto de columnas como de filas."
        while opcion != 0:
            self.showMenu()
            opcion = int(input("Ingrese Opcion: "))
            self.limparPantalla()
            if opcion == 1:
                matrizA = self.ingresarMatriz('A')
                matrizB = self.ingresarMatriz('B')
                if self.validarMatricesIguales(matrizA, matrizB):
                    result = self.sumarMatriz(np.array(matrizA), np.array(matrizB))
                    self.showResult(result)
                else:
                    print(msgerror)
            elif opcion == 2:
                matrizA = self.ingresarMatriz('A')
                matrizB = self.ingresarMatriz('B')
                if self.validarMatricesIguales(matrizA, matrizB):
                    result = self.restarMatriz(np.array(matrizA), np.array(matrizB))
                    self.showResult(result)
                else:
                    print(msgerror)
            elif opcion == 3:
                matrizA = self.ingresarMatriz('A')
                matrizB = self.ingresarMatriz('B')
                if self.validarMatricesMultiplicacion(np.array(matrizA), np.array(matrizB)):
                    result = self.multiplicarMatriz(np.array(matrizA), np.array(matrizB))
                    self.showResult(result)
                else:
                    print("El numero de columnas de la matriz A debe ser igual al numero de filas de la matriz B")
            elif opcion == 4:
                matrizA = self.ingresarMatriz('')
                result = self.determinanteMatriz(np.array(matrizA))
                self.showResult(result)
            elif opcion == 5:
                matrizA = self.ingresarMatriz('')
                result = self.transponerMatriz(np.matrix(matrizA))
                self.showResult(result)
            elif opcion == 6:
                matrizA = self.ingresarMatriz('')
                escalar =  int(input("Ingrese el escalar: "))
                result = self.multiplicarEscalarMatriz(np.array(matrizA), escalar)
                self.showResult(result)
            elif opcion == 7:
                self.generarMatrizAleatoria()
            elif opcion == 0:
                print("Vuelve pronto...")
            input("Presione una tecla para continuar ")

if __name__ == "__main__":
    c = Calculadora()
    c.main()