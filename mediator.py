from datetime import datetime

# Mediator (Mediador)
class ChatMediator:
    def enviar_mensaje(self, mensaje, usuario):
        pass

# ConcreteMediator (MediadorConcreto)
class SalaDeChat(ChatMediator):
    def __init__(self):
        self.usuarios = []

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def enviar_mensaje(self, mensaje, usuario):
        hora_actual = datetime.now().strftime("%H:%M:%S")
        for u in self.usuarios:
            if u != usuario:
                u.recibir_mensaje(f"{hora_actual} [{usuario.nombre}]: {mensaje}")

# Colleague (Colega)
class Usuario:
    def __init__(self, nombre, sala_de_chat):
        self.nombre = nombre
        self.sala_de_chat = sala_de_chat

    def enviar_mensaje(self, mensaje):
        self.sala_de_chat.enviar_mensaje(mensaje, self)

    def recibir_mensaje(self, mensaje):
        print(f"{self.nombre} recibe mensaje: {mensaje}")

# Cliente
if __name__ == "__main__":
    sala = SalaDeChat()

    usuario1 = Usuario("Usuario1", sala)
    usuario2 = Usuario("Usuario2", sala)
    usuario3 = Usuario("Usuario3", sala)

    sala.agregar_usuario(usuario1)
    sala.agregar_usuario(usuario2)
    sala.agregar_usuario(usuario3)

    usuario1.enviar_mensaje("¡Hola a todos!")
    usuario2.enviar_mensaje("¡Hola Usuario1!")
    usuario3.enviar_mensaje("¡Hola chicos!")

    # Salida esperada:
    # Usuario2 recibe mensaje: 10:00:00 [Usuario1]: ¡Hola a todos!
    # Usuario3 recibe mensaje: 10:00:00 [Usuario1]: ¡Hola a todos!
    # Usuario1 recibe mensaje: 10:00:00 [Usuario2]: ¡Hola Usuario1!
    # Usuario3 recibe mensaje: 10:00:00 [Usuario2]: ¡Hola Usuario1!
    # Usuario1 recibe mensaje: 10:00:00 [Usuario3]: ¡Hola chicos!
    # Usuario2 recibe mensaje: 10:00:00 [Usuario3]: ¡Hola chicos!
