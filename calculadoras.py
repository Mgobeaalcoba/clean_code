class CalculadoraEstatica:
    # Puedo acceder a sus métodos sin instanciarla
    @staticmethod
    def suma(a, b):
        return a + b

    @staticmethod
    def resta(a, b):
        return a - b

    @staticmethod
    def division(a, b):
        return a / b
    

class Calculadora:
    # Tiene constructor dado que para acceder a sus métodos debo instanciarla
    def __init__(self):
        pass

    def suma(self, a, b):
        return a + b

    def resta(self, a, b):
        return a - b

    def division(self, a, b):
        return a / b