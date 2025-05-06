class GeneradorContrasena:
    def crear(self, nombre, año):
        return f"{nombre}{año}@"


gen = GeneradorContrasena()
print(gen.crear("usuario", 2023))  
print(gen.crear("admin", 2024))    