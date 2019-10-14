from numpy import exp, array, random, dot, ravel
from FuncionesActivacion import FuncionesActivacion
import matplotlib.pyplot as plt

class RedNeuronalSimple(FuncionesActivacion):
    def __init__(self, entradas, salidas, bahias, n):
        self.pesos_signaticos = 2 * random.random((3,1)) - 1
        self.entradas = array(entradas)
        self.errores = []
        self.esperados= []
        self.salidas = array([salidas]).T
        self.bahias = bahias
        self.n = n
    
    def entrenar(self):
        for i in range(self.n):
            salida = self.pensar(self.entradas)
            error = self.salidas - salida
            ajuste = dot(self.entradas.T, error * self.sigmoide_derivado(salida))
            self.pesos_signaticos += ajuste
            self.esperados.append(ajuste)
            
    def pensar(self,entrada):
        return self.sigmoide(dot(entrada, self.pesos_signaticos))

    def imprimirResultado(self):
        print("Hola Mundo")
        # plt.plot(self.errores,'-',color='red')
        plt.plot(self.esperados,'*', color='green')
        plt.show()

# if __name__ == '__main__':
#     red_neuronal = RedNeuronal()
#     entradas = array([[0,0,1], [1,1,1], [1,0,1], [0,1,1]])
#     salidas = array([[0,1,1,0]]).T
#     red_neuronal.entrenamiento(entradas,salidas,1000)
#     print(red_neuronal.pesos_signaticos)
#     print(red_neuronal.pensar(array([1,0,0])))
    
        



#%%
