class Billete{
    constructor(v, c){

    this.valor = v;
    this.cantidad = c;

    }
}

function entregarDinero(){
    var t = document.getElementById("dinero");
    dinero = parseInt(t.value);  
    for(var bi of caja){
        if(dinero > 0){
            div = Math.floor(dinero / bi.valor);
            if(div > bi.cantidad){
                papeles = bi.cantidad;
            }else{
                papeles = div;    
            }
            entregado.push(new Billete(bi.valor, papeles));
            dinero = dinero - (bi.valor * papeles);
        }
    }

    if(dinero > 0){
        resultado.innerHTML = ("No tengo dinero");
    }else{
        for( var e of entregado){
            if(e.cantidad > 0){
                resultado.innerHTML += e.cantidad + " Billetes con valor $ " + e.valor + "<br />";
            }
        }
    }
}

var entregado = [];
var caja = [];
caja.push(new Billete(50, 50));
caja.push(new Billete(20, 90));
caja.push(new Billete(10, 90));

var div = 0;
var dinero = 0;
var papeles = 0;

var resultado = document.getElementById("resultado");
var b = document.getElementById("extraer");
b.addEventListener("click", entregarDinero);