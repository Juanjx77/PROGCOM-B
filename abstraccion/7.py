import random

class Dado:
    def tirar(self):
        return random.randint(1, 6)


dado = Dado()
print(dado.tirar())
print(dado.tirar())
print(dado.tirar())