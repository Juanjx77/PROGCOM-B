class Calculadora:
    def operar(self, a, b, tipo):
        if tipo == "suma":
            return a + b
        elif tipo == "resta":
            return a - b
        elif tipo == "multiplicacion":
            return a * b
        elif tipo == "division":
            return a / b if b != 0 else "Error: división por cero"
        else:
            return "Operación no válida"

calc = Calculadora()
print(calc.operar(5, 3, "suma"))  
print(calc.operar(5, 3, "resta"))  
print(calc.operar(5, 3, "multiplicacion")) 
print(calc.operar(6, 2, "division"))  