class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Libro(Producto):
    def __init__(self, nombre, precio):
        super().__init__(nombre, precio)  
    
    def mostrar_info(self):
        print(f"Libro: {self.nombre}, Precio: ${self.precio:.2f}")


mi_libro = Libro("Python para Principiantes", 29.99)
mi_libro.mostrar_info()




class Producto {
    String nombre;
    double precio;
    
    Producto(String nombre, double precio) {
        this.nombre = nombre;
        this.precio = precio;
    }
}

class Libro extends Producto {
    Libro(String nombre, double precio) {
        super(nombre, precio); // Llama al constructor de Producto
    }
    
    void mostrarInfo() {
        System.out.printf("Libro: %s, Precio: $%.2f%n", nombre, precio);
    }
}

public class Main {
    public static void main(String[] args) {
        Libro miLibro = new Libro("Python para Principiantes", 29.99);
        miLibro.mostrarInfo(); // Salida: "Libro: Python..., Precio: $29.99"
    }
}