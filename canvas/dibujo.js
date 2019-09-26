var d = document.getElementById("dibujito");
var lienzo = d.getContext("2d");

/*
lienzo.beginPath();
lienzo.strokeStyle = "red";
lienzo.moveTo(100, 100);
lienzo.lineTo(200, 200);
lienzo.stroke();
lienzo.closePath();
*/

dibujarLinea("blue", 20, 300, 330,5);

function dibujarLinea(color, x_inicial, y_incial, x_final, y_final){
    lienzo.beginPath();
    lienzo.strokeStyle = color;
    lienzo.moveTo(x_inicial, y_incial);
    lienzo.lineTo(x_final, y_final);
    lienzo.stroke();
    lienzo.closePath();
}