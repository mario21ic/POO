require './Perro'
require './Gato'
require './Ave'
require './Reptil'

perro = Veterinaria::Perro.new "Chico", "Rambo", 2
#puts perro.presentarse()
#puts perro.comunicarse()

gato = Veterinaria::Gato.new "Gandalf", 1
#puts gato.presentarse()

ave = Veterinaria::Ave.new "Piolin", 1
reptil = Veterinaria::Reptil.new "Juancho", 1
