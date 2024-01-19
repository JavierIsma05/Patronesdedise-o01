# Implementor (Implementador)
class Implementor:
    def operacion_implementada(self):
        pass

# ConcreteImplementorA (ImplementadorConcretoA)
class ImplementadorConcretoA(Implementor):
    def operacion_implementada(self):
        print("Operación implementada por ImplementadorConcretoA")

# ConcreteImplementorB (ImplementadorConcretoB)
class ImplementadorConcretoB(Implementor):
    def operacion_implementada(self):
        print("Operación implementada por ImplementadorConcretoB")

# Abstraction (Abstracción)
class Abstraccion:
    def __init__(self, implementador):
        self.implementador = implementador

    def operacion(self):
        pass

# RefinedAbstraction (AbstracciónRefinada)
class AbstraccionRefinada(Abstraccion):
    def operacion(self):
        print("Operación en AbstraccionRefinada")
        self.implementador.operacion_implementada()

# Cliente
implementadorA = ImplementadorConcretoA()
implementadorB = ImplementadorConcretoB()

abstraccionA = AbstraccionRefinada(implementadorA)
abstraccionB = AbstraccionRefinada(implementadorB)

abstraccionA.operacion()
abstraccionB.operacion()
