class Palabra:
    def __init__(self, texto):
        self.texto = texto.lower()
    
    def contar_vocales(self):
        vocales = "aeiouáéíóú"
        return sum(1 for letra in self.texto if letra in vocales)


pal1 = Palabra("Python")
pal2 = Palabra("Murciélago")
print(pal1.contar_vocales())  
print(pal2.contar_vocales())  