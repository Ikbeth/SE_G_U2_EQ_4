from pynput.keyboard import Controller
controlador = Controller()
import serial as s
arduino = None
arduino = s.Serial("COM3",baudrate=9600, timeout=1)

while True:
    cadena = arduino.readline()
    #print(cadena) ## imprime como...
    cadena = cadena.decode()
    cadena = cadena.replace("\n","")
    cadena = cadena.replace("\r","") ##\n y \r juntos hacen enter
    print(cadena)

    if not cadena == "":
        valores = cadena.split(" ")
        print(valores)
        if valores[0] == "1":
            controlador.press('A')
            controlador.release('A')
        elif valores[1] == "1":
            controlador.press('B')
            controlador.release('B')

