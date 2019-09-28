var teclas = {LEFT: 37, UP: 38, RIGHT: 39, DOWN: 40};
var cuadrito = document.getElementById("papelito");
var papel = cuadrito.getContext("2d");
var x = 90;
var y = 90;

document.addEventListener("keydown", dibujarTeclado);
document.addEventListener("mousedown", dibujarTeclado);
document.addEventListener("mousemove", dibujarTeclado);

dibujarLinea("red", x-1, y-1, x+1, y+1, papel);

function dibujarLinea(color, x_inicial, y_incial, x_final, y_final, lienzo){
    lienzo.beginPath();
    lienzo.strokeStyle = color;
    lienzo.lineWidth = 3;
    lienzo.moveTo(x_inicial, y_incial);
    lienzo.lineTo(x_final, y_final);
    lienzo.stroke();
    lienzo.closePath(); 
}

function dibujarTeclado(evento){
    colorlinea = "blue";
    movimiento = 10;
    
switch(evento.keyCode){
    case teclas.LEFT:
        dibujarLinea(colorlinea, x, y, x - movimiento, y, papel);
        x = x - 10;
    break;
    case teclas.UP:
        dibujarLinea(colorlinea, x, y, x, y - movimiento, papel);
        y = y - 10;
    break;
    case teclas.RIGHT:
        dibujarLinea(colorlinea, x, y, x + movimiento, y, papel);
        x = x + 10;
    break;
    case teclas.DOWN:
        dibujarLinea(colorlinea, x, y, x, y + movimiento, papel);
        y = y + 10;
        console.log(y);
    break;
    default:
        console.log(evento);
    }
}