var jf = require("johnny-five");
var circuito = new jf.Board();
circuito.on("ready", prender);

//Pines utilizados
var rojo, amarillo, verde;
var rojo2, amarillo2, verde2;
var tiempoEspera;
var tiempoCambio;
var servo;

function prender(){
    servo = new jf.Servo(6);
    
    rojo = new jf.Led(11);
    amarillo = new jf.Led(12);
    verde = new jf.Led(13);
    rojo2 = new jf.Led(8);
    amarillo2 = new jf.Led(9);
        verde2 = new jf.Led(10);

    roj
    rojo.blink(10000);
    amarillo.off();
    verde.off();

    rojo.off();
    amarillo.blink(10000);
    verde.off();

    rojo.off();
    amarillo.off();
    verde.blink(100000);
}