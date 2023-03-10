from pynput.keyboard import Controller
controlador = Controller()
import serial as s

arduino = None
arduino = s.Serial("COM3",baudrate=9600, timeout=1)

while True:
    cadena = arduino.readline()
    cadena = cadena.decode()
    cadena = cadena.replace("\n","")
    cadena = cadena.replace("\r","")
    print(cadena)

    valores = cadena.split(" ")
    if valores[0] == "1":
        controlador.press('A')
        controlador.release('A')

    elif valores[1] == "1":
        controlador.press('B')
        controlador.release('B')