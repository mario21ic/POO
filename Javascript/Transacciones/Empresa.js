var Empresa = function(razon_social, ruc) {
    this.razon_social = razon_social;
    this.ruc = ruc;
    this.pasos = 0;

    this.registrar_pasos = function(pasos) {
        this.pasos = pasos;
    }

    this.calcular_pago = function() {
        if (this.pasos <= 1000) {
            return 500;
        }
        var pasos_adicionales = Math.ceil((this.pasos - 1000) / 100);
        return 500 + pasos_adicionales * 20;
    }
}
