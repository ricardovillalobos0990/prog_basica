document.addEventListener("keyup", dibujarTeclado);
var teclas = {LEFT: 37, UP: 38, RIGHT: 39, DOWN: 40};

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