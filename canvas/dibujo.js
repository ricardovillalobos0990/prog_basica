var texto = document.getElementById("texto_lineas");
var boton = document.getElementById("botoncito");
boton.addEventListener("click", dibujoPorClick);

var d = document.getElementById("dibujito");
var ancho = d.width;
var lienzo = d.getContext("2d");


function dibujarLinea(color, x_inicial, y_incial, x_final, y_final){
    lienzo.beginPath();
    lienzo.strokeStyle = color;
    lienzo.moveTo(x_inicial, y_incial);
    lienzo.lineTo(x_final, y_final);
    lienzo.stroke();
    lienzo.closePath();
}

function dibujoPorClick(){
    var lineas = parseInt(texto.value);
    var l = 0;
    var yi, xf;
    var espacio = ancho / lineas;

    for(l=0; l < lineas; l++){
    yi = espacio * l ;
    xf = espacio * (l+1);
    dibujarLinea("red", 0, yi, xf, 300);
    }

    dibujarLinea("red", 1, 1, 1, 299);
    dibujarLinea("red", 1, 299, 299, 299);
    dibujarLinea("red", 1, 1, 299,1);
    dibujarLinea("red", 299, 1, 299, 299);
}

/*
for(l=0; l < 30; l++){
    xi = 10 * l;
    yf = 300-(10 *l);
    dibujarLinea("red", xi, 300, 300, yf);
}

for(l=0; l < 30; l++){
    yi = 300 - (10 * l);
    xf = 290 - (10 * l);
    dibujarLinea("red", 300, yi, xf, 0);
}

for(l=0; l < 30; l++){
    yi = 300 - (10 * l);
    xf = 10 * l;
    dibujarLinea("red", 0, yi, xf, 0);
}
*/