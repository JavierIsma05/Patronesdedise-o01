// Interfaz existente
class Adaptee {
    specificRequest() {
      return 'Solicitud específica';
    }
  }
  
  // Interfaz deseada
  class Target {
    request() {}
  }
  
  // Adaptador que convierte la interfaz de Adaptee a Target
  class Adapter extends Target {
    constructor(adaptee) {
      super();
      this.adaptee = adaptee;
    }
  
    request() {
      return this.adaptee.specificRequest();
    }
  }
  
  // Uso del Adapter
  const adaptee = new Adaptee();
  const adapter = new Adapter(adaptee);
  
  console.log(adapter.request()); // Salida: Solicitud específica
  