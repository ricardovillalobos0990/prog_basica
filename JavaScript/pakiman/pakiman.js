class Pakiman{
    constructor(n, v, a){
        this.imagen = new Image();

        this.nombre = n;
        this.ataque = a;
        this.vida = v;
        this.imagen.src = imagenes[this.nombre];

    }

    hablar(){
        alert(this.nombre);
    }

    mostrar(){
        document.body.appendChild(this.imagen);
        document.write("<p>");
        document.write("<strong>" + this.nombre + "</strong> <br />");
        document.write("VIDA: " + this.vida + "<br />");
        document.write("ATAQUE: " + this.ataque + "<hr />");
        document.write("</p>");
    }
}