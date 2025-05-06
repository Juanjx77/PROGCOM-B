class Cuenta:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial  

class CuentaAhorro(Cuenta):
    pass  


mi_ahorro = CuentaAhorro(1000)


print(f"Saldo actual: ${mi_ahorro.saldo:.2f}")






class Cuenta {
    double saldo;
    
    Cuenta(double saldoInicial) {
        this.saldo = saldoInicial;
    }
}

class CuentaAhorro extends Cuenta {
    CuentaAhorro(double saldoInicial) {
        super(saldoInicial);
    }
}

public class Main {
    public static void main(String[] args) {
        CuentaAhorro miAhorro = new CuentaAhorro(1000);
        System.out.printf("Saldo actual: $%.2f%n", miAhorro.saldo); // Salida: "Saldo actual: $1000.00"
    }
}