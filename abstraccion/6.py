class Palindromo:
    def __init__(self, palabra):
        self.palabra = palabra.lower().replace(" ", "")
    
    def es_palindromo(self):
        return self.palabra == self.palabra[::-1]


pal1 = Palindromo("reconocer")
pal2 = Palindromo("luz")
pal3 = Palindromo("oso")
print(pal1.es_palindromo())  
print(pal2.es_palindromo())  
print(pal3.es_palindromo())  