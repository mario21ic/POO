<?php

require_once './models/Alumno.php';
require_once './models/Curso.php';
require_once './controllers/MatriculaController.php';
require_once './views/MatriculaView.php';

$vista = new MatriculaView();
$vista->matricular();
