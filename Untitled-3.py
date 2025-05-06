class Vehiculo:
    def arrancar(self):
        print("Vehículo encendido")

class Moto(Vehiculo):
    def arrancar(self):
        print("Moto encendida")


mi_moto = Moto()
mi_moto.arrancar()



class Vehiculo {
    void arrancar() {
        System.out.println("Vehículo encendido");
    }
}

class Moto extends Vehiculo {
    @Override
    void arrancar() {
        System.out.println("Moto encendida");
    }
}

public class Main {
    public static void main(String[] args) {
        Moto miMoto = new Moto();
        miMoto.arrancar(); // Salida: "Moto encendida"
    }
}