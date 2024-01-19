# Adaptee (Clase existente con interfaz incompatible)
class Adaptee:
    def operacion_especifica(self):
        return "Operación específica"

# Target (Interfaz deseada)
class Target:
    def solicitud(self):
        return "Solicitud estándar"

# Adapter (Adaptador que hace que Adaptee se comporte como Target)
class Adaptador(Target):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def solicitud(self):
        return f"Adaptado: {self.adaptee.operacion_especifica()}"

# Cliente que utiliza Target
def codigo_cliente(target):
    print(target.solicitud())

# Uso del Adapter para que Adaptee se comporte como Target
adaptee = Adaptee()
adaptador = Adaptador(adaptee)

print("Adaptee dice:", adaptee.operacion_especifica())
print("Target dice:", codigo_cliente(Target()))  # Cliente utilizando Target directamente
print("Adaptador dice:", codigo_cliente(adaptador))  # Cliente utilizando Adaptador que hace que Adaptee se comporte como Target
