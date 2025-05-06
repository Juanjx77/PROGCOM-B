class Computadora:
    def encender(self):
        print("La computadora se está encendiendo...")

class Portatil(Computadora):
    pass 


mi_portatil = Portatil()
mi_portatil.encender()  




class Computadora {
    void encender() {
        System.out.println("La computadora se está encendiendo...");
    }
}

class Portatil extends Computadora {
    // Sin modificaciones
}

public class Main {
    public static void main(String[] args) {
        Portatil miPortatil = new Portatil();
        miPortatil.encender(); // Salida: "La computadora se está encendiendo..."
    }
}