class Empleado:
    def trabajar(self):
        print("Realizando tareas generales de empleado")

class Gerente(Empleado):
    def trabajar(self):
        print("Coordina equipos y toma decisiones estratégicas")

class Obrero(Empleado):
    def trabajar(self):
        print("Realiza trabajos manuales y operativos")


jefe = Gerente()
trabajador = Obrero()

jefe.trabajar()        
trabajador.trabajar()  


class Empleado {
    void trabajar() {
        System.out.println("Realizando tareas generales");
    }
}

class Gerente extends Empleado {
    @Override
    void trabajar() {
        System.out.println("Coordina equipos y toma decisiones");
    }
}

class Obrero extends Empleado {
    @Override
    void trabajar() {
        System.out.println("Realiza trabajos manuales");
    }
}

public class Main {
    public static void main(String[] args) {
        Gerente jefe = new Gerente();
        Obrero trabajador = new Obrero();
        
        jefe.trabajar();      // Salida: "Coordina equipos..."
        trabajador.trabajar(); // Salida: "Realiza trabajos manuales"
    }
}