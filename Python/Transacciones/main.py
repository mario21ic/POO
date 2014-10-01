from Empresa import Empresa

def main():
    empresaA = Empresa("Comunicore", "1234566668")
    empresaB = Empresa("Yaroslab", "1234563338")
    empresaC = Empresa("UPC", "333666888")

    empresaA.registrar_pasos(1000)
    print empresaA.calcular_pago()

if __name__ == '__main__':
    main()
