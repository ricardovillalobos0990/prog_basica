class Operaciones:
    def __init__(self, num1, num2):
        self.sum = sum
        self.num1 = num1
        self.num2 = num2

    def suma(self, num1, num2):
        sum = num1 + num2
        print(type(num1))
        self.sum = sum

    def res(self, num1, num2):
        res = int(self.num1.get()) - int(self.num2.get())
        return self.valor.set(res)