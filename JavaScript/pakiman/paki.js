var imagenes = [];
imagenes["Cauchin"] = "vaca.png";
imagenes["Pocacho"] = "pollo.webp";
imagenes["Tocinauro"] = "cerdo.webp";

var coleccion = [];
coleccion.push(new Pakiman("Cauchin", 100, 20));
coleccion.push(new Pakiman("Pocacho", 80, 20));
coleccion.push(new Pakiman("Tocinauro", 50 ,90));

for(var mos of coleccion){
    mos.mostrar();    
}