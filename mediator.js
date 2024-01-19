// Mediator: ChatRoom
class ChatRoom {
    showMessage(user, message) {
      return `[${user.getName()}] dice: ${message}`;
    }
  }
  
  // Colleague: Usuario
  class User {
    constructor(name, chatMediator) {
      this.name = name;
      this.chatMediator = chatMediator;
    }
  
    send(message) {
      return this.chatMediator.showMessage(this, message);
    }
  
    getName() {
      return this.name;
    }
  }
  
  // Uso del Patrón Mediator
  const chatMediator = new ChatRoom();
  
  const user1 = new User('Usuario1', chatMediator);
  const user2 = new User('Usuario2', chatMediator);
  
  console.log(user1.send('Hola, ¿cómo estás?'));  // Salida: [Usuario1] dice: Hola, ¿cómo estás?
  console.log(user2.send('¡Hola! Estoy bien, gracias.'));  // Salida: [Usuario2] dice: ¡Hola! Estoy bien, gracias.
  