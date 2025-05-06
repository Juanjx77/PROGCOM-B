class SerVivo:
    def respirar(self):
        print("Respirando...")

class Humano(SerVivo):
    pass 


persona = Humano()
persona.respirar()  



class SerVivo {
    void respirar() {
        System.out.println("Respirando...");
    }
}

class Humano extends SerVivo {
    // Sin modificaciones
}

public class Main {
    public static void main(String[] args) {
        Humano persona = new Humano();
        persona.respirar(); // Salida: "Respirando..."
    }
}