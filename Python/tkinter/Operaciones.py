class Operaciones:
    def __init__(self, num1, num2):
        self.sum = sum
        self.res = res
        self.num1 = num1
        self.num2 = num2

    def suma(self, num1, num2):
        self.sum = num1 + num2
        return self.sum

    def resta(self, num1, num2):
        self.res = num1 - num2
        return self.res