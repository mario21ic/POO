<?php

require_once 'Perro.php';
require_once 'Gato.php';
require_once 'Ave.php';
require_once 'Reptil.php';
require_once 'Cliente.php';

$perro = new Perro("Chico", "Rambo", 1);
#print $perro->presentarse();
#print $perro->comunicarse();

$gato = new Gato("Gandalf", 1);
#print $gato->presentarse();

$ave = new Ave("Piolin", 1);
$reptil = new Reptil("Juancho", 1);

$cliente = new Cliente("Mario");
$cliente->agregarMascota($perro);
$cliente->agregarMascota($gato);
$cliente->agregarMascota($ave);
$cliente->agregarMascota($reptil);

print $cliente->reporteMascotas();
