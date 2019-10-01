const atencion = require('express')
const aplicacion = atencion()
 
aplicacion.get('/', inicio);
aplicacion.get('/cursos', cursos);


function inicio(peticion, resultado){
    resultado.send("Este es el HOME");
}

function cursos(peticion, resultado){
    resultado.send("Estos son los cursos");
}

aplicacion.listen(8989);