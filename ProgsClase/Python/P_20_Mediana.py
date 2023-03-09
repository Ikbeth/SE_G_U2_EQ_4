##librerias: PyQt5, matplotlib, pyserial

import serial as s

arduino = None
arduino = s.Serial("COM3",baudrate=9600, timeout=1)

while True:
    cadena = arduino.readline()
    cadena = cadena.decode()
    cadena = cadena.replace("\n","")
    cadena = cadena.replace("\r","")
    print("MEDIANA = ", cadena)