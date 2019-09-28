var teclas = {LEFT: 37, UP: 38, RIGHT: 39, DOWN: 40};
var cuadrito = document.getElementById("recuadro");
var papel = cuadrito.getContext("2d");
var x = 0;
var y = 0;

var vaca = {url:"vaca.png", cargaOK: false };
var fondo = {url:"tile.png", cargaOK: false };
var pollo = {url:"pollo.webp", cargaOK: false };
var cerdo = {url:"cerdo.webp", cargaOK: false };

document.addEventListener("keydown", dibujarTeclado);

vaca.imagen = new Image();
vaca.imagen.src = vaca.url;
vaca.imagen.addEventListener("load", cargarVacas);

fondo.imagen = new Image();
fondo.imagen.src = fondo.url;
fondo.imagen.addEventListener("load", cargarFondo);

pollo.imagen = new Image();
pollo.imagen.src = pollo.url;
pollo.imagen.addEventListener("load", cargarPollos);

cerdo.imagen = new Image();
cerdo.imagen.src = cerdo.url;
cerdo.imagen.addEventListener("load", cargarCerdos);

function cargarVacas(){
    vaca.cargaOK = true;
    dibujar();
}

function cargarFondo(){
    fondo.cargaOK = true;
    dibujar();
}

function cargarPollos(){
    fondo.cargaOK = true;
    dibujar();
}

function cargarCerdos(){
    cerdo.cargaOK = true;
    dibujar();
}

function dibujarTeclado(evento){
    colorlinea = "blue";
    movimiento = 10;
    
switch(evento.keyCode){
    case teclas.LEFT:
        dibujar();
        x = x - 10;
    break;
    case teclas.UP:
        dibujar();
        y = y - 10;
    break;
    case teclas.RIGHT:
        dibujar();
        x = x + 10;
    break;
    case teclas.DOWN:
        dibujar();
        y = y + 10;
    break;
    default:
        console.log(evento);
    }
}

function dibujar(){
    papel.drawImage(fondo.imagen, 0, 0);
    papel.drawImage(pollo.imagen, 100, 100);
    papel.drawImage(cerdo.imagen, 200, 200);
    if(vaca.cargaOK == true){
    papel.drawImage(vaca.imagen, x, y);
    }
}