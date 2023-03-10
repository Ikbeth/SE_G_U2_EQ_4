import random
import sys
from time import sleep
import serial as conecta

from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "Practica_3_Ahorcado.ui"  # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #botones
        self.btn_accion.clicked.connect(self.accion)
        self.btn_Iniciar.clicked.connect(self.iniciar)
        self.btn_comparar.clicked.connect(self.comparar)

        #Variables
        self.arduino = None
        self.cont = 65
        self.x = 1
        self.errores = 0


        self.segundoPlano = QtCore.QTimer()
        #self.segundoPlano.timeout.connect(self.obtenerCadena)

        self.segundoPlano.timeout.connect(self.obtenerCadena)

    def accion(self):
        try:
            txt_btn = self.btn_accion.text()
            if txt_btn == "CONECTAR": ##arduino == None
                self.txt_estado.setText("CONECTADO")
                self.btn_accion.setText("DESCONECTAR")
                #puerto = self.txt_puerto.text()
                puerto = "COM" + self.txt_puerto.text()
                self.arduino = conecta.Serial(puerto, baudrate=9600, timeout=0.5)
                self.segundoPlano.start(10)
            elif txt_btn == "DESCONECTAR":
                self.txt_estado.setText("DESCONECTADO")
                self.btn_accion.setText("RECONECTAR")
                self.segundoPlano.stop()
                self.arduino.close()
            else: #RECONECTAR
                self.txt_estado.setText("RECONECTADO")
                self.btn_accion.setText("DESCONECTAR")
                self.arduino.open()
                self.segundoPlano.start(10)
        except Exception as error:
            print(error)
        #self.arduino.isOpen()

    def iniciar(self):
        if not self.arduino == None:
            if self.arduino.isOpen():
                self.btn_Iniciar.setText("Reiniciar")
                #reinicio de variables
                self.cont = 65
                self.x = 1
                self.errores = 0
                #Reinicio de Variables
                self.car1.setText("_")
                self.car1.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.car2.setText("_")
                self.car2.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.car3.setText("_")
                self.car3.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.car4.setText("_")
                self.car4.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.car5.setText("_")
                self.car5.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.car6.setText("_")
                self.car6.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.txt_confirmacion.setText("")
                #Reiniciar Imagenes
                self.fases.setStyleSheet("border-image: url(:/fases/Imagenes/fase1.png);")
                self.vida1.setStyleSheet("border-image: url(:/vidas/Imagenes/vidas.png);")
                self.vida2.setStyleSheet("border-image: url(:/vidas/Imagenes/vidas.png);")
                self.vida3.setStyleSheet("border-image: url(:/vidas/Imagenes/vidas.png);")


                palabras = ['CARROS','PLATOS','PERROS','SANDIA','PIEDRA','ACEITE']
                posicion = random.randint(0,5)
                self.palabra = palabras[posicion]
                print(self.palabra)

                self.btn_comparar.setEnabled(True)

    def obtenerCadena(self):
        if not self.arduino == None:
            if self.arduino.isOpen():
                if self.arduino.inWaiting():
                    cadena = self.arduino.readline()
                    cadena = cadena.decode()
                    cadena = cadena.replace("\n", "")
                    cadena = cadena.replace("\r", "")

                    if cadena == "Seleccionar":
                        self.x += 1
                        if self.x > 6:
                            self.x = 1

                    elif cadena == "Siguiente":
                        self.cont += 1
                        if self.cont > 90:
                            self.cont = 90

                        if self.x == 1:
                            self.car1.setText(chr(self.cont))
                        elif self.x == 2:
                            self.car2.setText(chr(self.cont))
                        elif self.x == 3:
                            self.car3.setText(chr(self.cont))
                        elif self.x == 4:
                            self.car4.setText(chr(self.cont))
                        elif self.x == 5:
                            self.car5.setText(chr(self.cont))
                        elif self.x == 6:
                            self.car6.setText(chr(self.cont))

                    elif cadena == "Anterior":
                        self.cont -= 1
                        if self.cont < 65:
                            self.cont = 65

                        if self.x == 1:
                            self.car1.setText(chr(self.cont))
                        elif self.x == 2:
                            self.car2.setText(chr(self.cont))
                        elif self.x == 3:
                            self.car3.setText(chr(self.cont))
                        elif self.x == 4:
                            self.car4.setText(chr(self.cont))
                        elif self.x == 5:
                            self.car5.setText(chr(self.cont))
                        elif self.x == 6:
                            self.car6.setText(chr(self.cont))

    def comparar(self):
        if not self.arduino == None:
            if self.arduino.isOpen():
                self.btn_Iniciar.setEnabled(False)
                c1 = self.car1.text()
                c2 = self.car2.text()
                c3 = self.car3.text()
                c4 = self.car4.text()
                c5 = self.car5.text()
                c6 = self.car6.text()
                aciertos = 0

                if c1 == self.palabra[0]:
                    self.car1.setStyleSheet("background-color: rgb(0, 255, 0);")
                    aciertos += 1
                elif c1 == "_":
                    self.car1.setStyleSheet("background-color: rgb(0, 200, 200);")
                else:
                    self.car1.setStyleSheet("background-color: rgb(255, 0, 0);")
                    self.errores += 1

                if c2 == self.palabra[1]:
                    self.car2.setStyleSheet("background-color: rgb(0, 255, 0);")
                    aciertos += 1
                elif c2 == "_":
                    self.car2.setStyleSheet("background-color: rgb(0, 200, 200);")
                else:
                    self.car2.setStyleSheet("background-color: rgb(255, 0, 0);")
                    self.errores += 1

                if c3 == self.palabra[2]:
                    self.car3.setStyleSheet("background-color: rgb(0, 255, 0);")
                    aciertos += 1
                elif c3 == "_":
                    self.car3.setStyleSheet("background-color: rgb(0, 200, 200);")
                else:
                    self.car3.setStyleSheet("background-color: rgb(255, 0, 0);")
                    self.errores += 1

                if c4 == self.palabra[3]:
                    self.car4.setStyleSheet("background-color: rgb(0, 255, 0);")
                    aciertos += 1
                elif c4 == "_":
                    self.car4.setStyleSheet("background-color: rgb(0, 200, 200);")
                else:
                    self.car4.setStyleSheet("background-color: rgb(255, 0, 0);")
                    self.errores += 1

                if c5 == self.palabra[4]:
                    self.car5.setStyleSheet("background-color: rgb(0, 255, 0);")
                    aciertos += 1
                elif c5 == "_":
                    self.car5.setStyleSheet("background-color: rgb(0, 200, 200);")
                else:
                    self.car5.setStyleSheet("background-color: rgb(255, 0, 0);")
                    self.errores += 1

                if c6 == self.palabra[5]:
                    self.car6.setStyleSheet("background-color: rgb(0, 255, 0);")
                    aciertos += 1
                elif c6 == "_":
                    self.car6.setStyleSheet("background-color: rgb(0, 200, 200);")
                else:
                    self.car6.setStyleSheet("background-color: rgb(255, 0, 0);")
                    self.errores += 1

                if aciertos >= 6:
                    self.txt_confirmacion.setText("Has Ganado")
                    self.btn_Iniciar.setEnabled(True)
                    self.arduino.write("1".encode())

                if self.errores > 0:
                    self.arduino.write("0".encode())

                if self.errores == 1:
                    self.fases.setStyleSheet("border-image: url(:/fases/Imagenes/fase1.png);")
                elif self.errores == 2:
                    self.fases.setStyleSheet("border-image: url(:/fases/Imagenes/fase2.png);")
                    self.vida1.setStyleSheet("border-image: rgb(255, 255, 255);")
                elif self.errores == 3:
                    self.fases.setStyleSheet("border-image: url(:/fases/Imagenes/fase3.png);")
                elif self.errores == 4:
                    self.fases.setStyleSheet("border-image: url(:/fases/Imagenes/fase4.png);")
                    self.vida2.setStyleSheet("border-image: rgb(255, 255, 255);")
                    self.vida1.setStyleSheet("border-image: rgb(255, 255, 255);")
                elif self.errores == 5:
                    self.fases.setStyleSheet("border-image: url(:/fases/Imagenes/fase5.png);")
                elif self.errores >= 6:
                    self.fases.setStyleSheet("border-image: url(:/fases/Imagenes/fase6.png);")
                    self.vida2.setStyleSheet("border-image: rgb(255, 255, 255);")
                    self.vida1.setStyleSheet("border-image: rgb(255, 255, 255);")
                    self.vida3.setStyleSheet("border-image: rgb(255, 255, 255);")
                    self.txt_confirmacion.setText("Has Perdido")
                    self.btn_Iniciar.setEnabled(True)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())