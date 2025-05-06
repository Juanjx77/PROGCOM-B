class Temperatura:
    def __init__(self, celsius):
        self.celsius = celsius
    
    def a_fahrenheit(self):
        return self.celsius * 1.8 + 32


temp = Temperatura(25)
print(temp.a_fahrenheit())  