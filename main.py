from general.auto import Auto
from electronica import funcionar

def main():
    miAuto = Auto("Toyota", "Corolla", "rojo")
    miAuto.arrancar()
    funcionar()
    miAuto.acelerar(50)
    miAuto.frenar()
    miAuto.apagar()

main()
