package main

import (
    "fmt"
)

type Donante struct {
    nombre string
    dni string
    telefono string
    email string
    monto int
}

type Administrador struct {
    Donante
}

func (a *Administrador) registrarDonante (d *Donante ) {
    return d
}

func (a *Administrador) montoTotal() {
    return a
}

func (a *Administrador) donanteTop() {
    return a
}

func (a *Administrador) buscarDonante() {
    return a
}

func (a *Administrador) montoPromedio() {
    return a
}

func main() {
    donante := Donante{
        nombre: "mario",
        dni: "44489174",
        telefono: "942943937",
        email: "mario21ic@gmail.com",
        monto: 250}
    fmt.Println("donante: %", donante.nombre)
}
