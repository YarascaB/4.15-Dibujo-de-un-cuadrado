class Cuadrado:
    def __init__(self):
        self.lado = 0

    def ingresar_datos(self):
        self.lado = int(input("Ingrese el número de asteriscos por lado del cuadrado: "))

    def dibujar_cuadrado(self):
        # Dibuja el lado superior
        print("* " * self.lado)

        # Dibuja los lados laterales
        for i in range(self.lado - 2):
            print("*" + "  " * (self.lado - 2) + " *")

        # Dibuja el lado inferior
        if self.lado > 1:
            print("* " * self.lado)


# Ejemplo de uso
cuadrado = Cuadrado()
cuadrado.ingresar_datos()
cuadrado.dibujar_cuadrado()



# Ejemplo de uso
cuadrado = Cuadrado()
cuadrado.ingresar_datos()
cuadrado.dibujar_cuadrado()

