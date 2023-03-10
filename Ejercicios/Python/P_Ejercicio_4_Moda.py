##librerias: PyQt5, matplotlib, pyserial

import serial as s

arduino = None
arduino = s.Serial("COM3",baudrate=9600, timeout=1)

while True:
    cadena = arduino.readline()
    #print(cadena) ## imprime como...
    cadena = cadena.decode()
    cadena = cadena.replace("\n","")
    cadena = cadena.replace("\r","") ##\n y \r juntos hacen enter
    print("MODA = ", cadena) ##<<---