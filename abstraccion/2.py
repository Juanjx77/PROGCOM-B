class Numero:
    def __init__(self, valor):
        self.valor = valor
    
    def es_par(self):
        return self.valor % 2 == 0


num1 = Numero(4)
num2 = Numero(7)
print(num1.es_par())  
print(num2.es_par())  