<?php

function __autoload($name) {
    $fullpath = 'classes/'.strtolower($name).'.php';
    if(file_exists($fullpath)) require_once($fullpath);
}

include 'classes/Perro.php';

$perro = new Perro("Chico", "Rambo", 1);
print $perro.presentarse();
