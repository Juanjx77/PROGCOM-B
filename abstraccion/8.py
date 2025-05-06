class ListaCuadrados:
    def generar(self, n):
        return [i**2 for i in range(1, n+1)]


generador = ListaCuadrados()
print(generador.generar(5))  
print(generador.generar(10))  