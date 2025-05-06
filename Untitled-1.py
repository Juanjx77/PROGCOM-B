class Animal:
    def mostrar(self):
        print("Este es un animal")

class Perro(Animal):
    pass


mi_perro = Perro()
mi_perro.mostrar()


class Animal {
    void mostrar() {
        System.out.println("Este es un animal");
    }
}

class Perro extends Animal {
    // Sin modificaciones
}

public class Main {
    public static void main(String[] args) {
        Perro miPerro = new Perro();
        miPerro.mostrar(); // Salida: "Este es un animal"
    }
}