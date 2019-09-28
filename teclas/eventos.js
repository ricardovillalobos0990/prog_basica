var teclas = {LEFT: 37, UP: 38, RIGHT: 39, DOWN: 40};


document.addEventListener("keyup", dibujarTeclado);
var cuadrito = document.getElementById("papelito");
var papel = cuadrito.getContext("2d");

dibujarLinea("red", 100, 100, 200, 200, papel);

function dibujarLinea(color, x_inicial, y_incial, x_final, lienzo){
    lienzo.beginPath();
    lienzo.strokeStyle = color;
    lienzo.moveTo(x_inicial, y_incial);
    lienzo.lineTo(x_final, y_final);
    lienzo.stroke();
    lienzo.closePath();
}

function dibujarTeclado(evento){
switch(evento.keyCode){
    case teclas.LEFT:
        console.log("IZQUIERDA");
    break;
    case teclas.UP:
        console.log("ARRIBA");
    break;
    case teclas.RIGHT:
        console.log("DERECHA");
    break;
    case teclas.DOWN:
        console.log("ABAJO");
    break;
    default:
        console.log("Otra tecla");
    }
}