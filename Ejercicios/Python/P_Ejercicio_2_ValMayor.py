##librerias: PyQt5, matplotlib, pyserial

import serial as s

arduino = None  
arduino = s.Serial("COM3",baudrate=9600, timeout=1)
lista=[]
totlecturas=2
i=0
while i<totlecturas:
    cadena =arduino.readline()
    #print(cadena) ## imprime como...
    cadena = cadena.decode()
    cadena = cadena.replace("\n","")
    cadena = cadena.replace("\r","") ##\n y \r juntos hacen enter
    print(cadena) ##<<---
    lista.append(cadena)
    i=+1
###lista=["2","3","4","6"]
lista=list(map(int,lista))
print(lista)
