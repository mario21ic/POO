from Perro import Perro
from Gato import Gato
from Ave import Ave
from Reptil import Reptil
from Cliente import Cliente

perro = Perro("Chico", "Rambo", 1)
#print perro.presentarse()
#print perro.comunicarse()

gato = Gato("Gandalf", 1)
#print gato.presentarse()

ave = Ave("Piolin", 1)
reptil = Reptil("Juancho", 1)

cliente = Cliente("Mario")
cliente.agregarMascota(perro)
cliente.agregarMascota(gato)
cliente.agregarMascota(ave)
cliente.agregarMascota(reptil)
print cliente.reporteMascotas()
