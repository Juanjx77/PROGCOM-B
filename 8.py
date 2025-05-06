class Animal:
    def sonido(self):
        print("Sonido genérico")

class Gato(Animal):
    def sonido(self):
        super().sonido()  
        print("Miau!")    


mi_gato = Gato()
mi_gato.sonido()




class Animal {
    void sonido() {
        System.out.println("Sonido genérico");
    }
}

class Gato extends Animal {
    @Override
    void sonido() {
        super.sonido(); // Llama al método del padre
        System.out.println("Miau!");
    }
}

public class Main {
    public static void main(String[] args) {
        Gato miGato = new Gato();
        miGato.sonido(); // Salida: "Sonido genérico" + "Miau!"
    }
}