from controllers.MatriculaController import MatriculaController

class MatriculaView(object):
    def __init__(self):
        self.matricula_controller = MatriculaController()

    def matricular(self):
        opcion = '1'
        while opcion != '3':
            self.mostrar_menu()
            opcion = self.leer_opcion()
            self.evaluar_opcion(opcion)

    def mostrar_menu(self):
        print """
        Bienvenido al sistema
        1 Matricular alumno
        2 Listar alumnos
        3 Salir
        """

    def leer_opcion(self):
        return raw_input("Seleccione una accion: ")

    def evaluar_opcion(self, opcion):
        if opcion == '1':
            codigo = raw_input("Ingrese el codigo: ")
            nombre = raw_input("Ingrese el nombre: ")
            apellido = raw_input("Ingrese el apellido: ")
            print self.matricula_controller.matricular(codigo, nombre, apellido)
        elif opcion == '2':
            print self.matricula_controller.reporte_matricula()
        else:
            print "Opcion no valida"

