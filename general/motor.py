class Motor:
    def __init__(self):
        self.encendido = False

    def encender(self):
        print("El motor está encendido.")
        self.encendido = True

    def apagar(self):
        print("El motor está apagado.")
        self.encendido = False
