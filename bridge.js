// Implementación: Dispositivos
class TV {
    turnOn() {
      return 'TV encendida';
    }
  
    turnOff() {
      return 'TV apagada';
    }
  }
  
  class Radio {
    turnOn() {
      return 'Radio encendida';
    }
  
    turnOff() {
      return 'Radio apagada';
    }
  }
  
  // Abstracción: Controles Remotos
  class RemoteControl {
    constructor(device) {
      this.device = device;
    }
  
    powerOn() {
      return this.device.turnOn();
    }
  
    powerOff() {
      return this.device.turnOff();
    }
  }
  
  // Uso del Patrón Bridge
  const tv = new TV();
  const radio = new Radio();
  
  const tvRemote = new RemoteControl(tv);
  console.log(tvRemote.powerOn());  // Salida: TV encendida
  
  const radioRemote = new RemoteControl(radio);
  console.log(radioRemote.powerOff());  // Salida: Radio apagada
  