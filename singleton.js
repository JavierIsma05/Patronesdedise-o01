class Singleton {
    static instancia;
    nombre ='';

    constructor(nombre=''){
        Singleton.instancia=this;
        this.nombre = nombre;
        return this;
    }
}
const instancia1=new Singleton('Javier')
const instancia2=new Singleton('Juan')

console.log(`Nombre en la instancia1 es: ${instancia1.nombre}`);
console.log(`Nombre en la instancia2 es: ${instancia2.nombre}`);