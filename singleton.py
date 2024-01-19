def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance

@singleton
class MyClass:
    def __init__(self, value):
        self.value = value

# Ejemplo de uso
instance1 = MyClass(1)
instance2 = MyClass(2)

print(instance1 is instance2)  # Debería imprimir True, ya que ambas variables apuntan a la misma instancia
print(instance1.value)          # Debería imprimir 1
print(instance2.value)          # Debería imprimir 1, ya que es la misma instancia compartida
