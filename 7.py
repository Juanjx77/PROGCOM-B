class Persona:
    def saludar(self):
        print("Hola")

class Profesor(Persona):
    def enseñar(self):
        print("Estoy enseñando")


profesor1 = Profesor()
profesor1.saludar()  
profesor1.enseñar()  



class Persona {
    void saludar() {
        System.out.println("Hola");
    }
}

class Profesor extends Persona {
    void enseñar() {
        System.out.println("Estoy enseñando");
    }
}

public class Main {
    public static void main(String[] args) {
        Profesor profesor1 = new Profesor();
        profesor1.saludar(); // Salida: "Hola"
        profesor1.enseñar(); // Salida: "Estoy enseñando"
    }
}