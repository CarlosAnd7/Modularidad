from .motor import Motor

class Auto:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.motor = Motor()

    def arrancar(self):
        print(f"El {self.marca} {self.modelo} de color {self.color} está arrancando.")
        self.motor.encender()

    def apagar(self):
        print(f"El {self.marca} {self.modelo} está apagado.")
        self.motor.apagar()

    def acelerar(self, velocidad):
        print(f"El {self.marca} {self.modelo} está acelerando a {velocidad} km/h.")

    def frenar(self):
        print(f"El {self.marca} {self.modelo} está frenando.")

