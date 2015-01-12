var Administrador = function(opciones) {
    this.donantes = [];

    this.agregar_donante = function(donante) {
        this.donantes.push(donante);
    };
    
    this.monto_total = function() {
        var monto_total = 0;
        for (var x=0; x<this.donantes.length; x++) {
            monto_total += this.donantes[x].monto;
        }
        return monto_total;
    };

    this.donante_top = function() {
        var donante_top;
        var monto_top = 0;
        for (var x=0; x<this.donantes.length; x++) {
            if (monto_top <= this.donantes[x].monto){
                monto_top = this.donantes[x].monto;
                donante_top = this.donantes[x];
            }
        }
        return donante_top;
    };

    this.buscar_donante = function(dni) {
        var donante;
        for (var x=0; x<this.donantes.length; x++){
            if (dni == this.donantes[x].dni) {
                donante = this.donantes[x];
            }
        }
        return donante;
    };

    this.monto_promedio = function() {
        return this.monto_total() / this.donantes.length
    };
};

