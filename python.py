class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

class Estudiante(Persona):
    pass

estudiante1 = Estudiante("Maria Lopez")
print(estudiante1.nombre)





class Persona {
    String nombre;
    
    Persona(String nombre) {
        this.nombre = nombre;
    }
}

class Estudiante extends Persona {
    Estudiante(String nombre) {
        super(nombre); // Llama al constructor de Persona
    }
}

public class Main {
    public static void main(String[] args) {
        Estudiante estudiante1 = new Estudiante("María López");
        System.out.println(estudiante1.nombre); // Salida: "María López"
    }
}