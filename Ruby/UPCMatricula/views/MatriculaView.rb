require_relative '../controllers/MatriculaController'

class MatriculaView

    def initialize
        @matricula_controller = MatriculaController.new
    end

    def matricular
        opcion = "1\n"
        while opcion != "3\n"
            self.mostrar_menu()
            opcion = self.leer_opcion()
            self.evaluar_opcion(opcion)
        end
    end

    def mostrar_menu
        menu = "Bienvenido al sistema\n"
        menu += "1 Matricular alumno\n"
        menu += "2 Listar alumno\n"
        menu += "3 Salir"
        puts menu
    end

    def leer_opcion
        return STDIN.gets()
    end

    def evaluar_opcion(opcion)
        if opcion == "1\n"
            puts "Ingrese codigo:"
            codigo = gets()
            puts "Ingrese nombre:"
            nombre = gets()
            puts "Ingrese apellido:"
            apellido = gets()
            puts @matricula_controller.matricular(codigo, nombre, apellido)
        elsif opcion == "2\n"
            puts @matricula_controller.reporte_matricula()
        else
            puts "Opcion no valida"
        end
    end

end
