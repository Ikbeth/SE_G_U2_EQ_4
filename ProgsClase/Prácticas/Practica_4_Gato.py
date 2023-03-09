import sys
import  serial as serial
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "Practica_4_Gato.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.arduino = None
        self.turno =  0
        self.respuesta = ""

        self.BotonConectar.clicked.connect(self.conectar)

        self.BotonIniciar.clicked.connect(self.juego)

        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.control)


    # Área de los Slots

    def conectar(self):
        try:
            txt_btn = self.BotonConectar.text()
            if txt_btn == "CONECTAR":
                self.BotonConectar.setText("DESCONECTAR")
                puerto = "COM" + self.TextPuerto.text()
                self.arduino = serial.Serial(puerto, baudrate=9600, timeout=0.5)
            elif txt_btn == "DESCONECTAR":
                self.BotonConectar.setText("RECONECTAR")
                self.arduino.close()
            else: #RECONECTAR
                self.BotonConectar.setText("DESCONECTAR")
                self.arduino.open()

        except Exception as error:
            print(error)

    def juego(self):
        try:
            TextJugar = self.BotonIniciar.text()
            if TextJugar == "INICIAR":
                self.BotonIniciar.setText("DETENER")
                self.segundoPlano.start(20)

                self.Text00.setText("")
                self.Text01.setText("")
                self.Text02.setText("")
                self.Text10.setText("")
                self.Text11.setText("")
                self.Text12.setText("")
                self.Text20.setText("")
                self.Text21.setText("")
                self.Text22.setText("")

                self.turno = 0
            else:
                self.BotonIniciar.setText("INICIAR")
                self.segundoPlano.stop()
        except Exception as error:
            print(error)

    def control(self):
        try:
            if not self.arduino == None:
                if self.arduino.isOpen():
                    if self.arduino.inWaiting():
                        coordenadas = self.arduino.readline().decode()
                        coordenadas = coordenadas.replace("\r", "")
                        coordenadas = coordenadas.replace("\n", "")
                        #print(coordenadas)

                        text00 = self.Text00.text()
                        text01 = self.Text01.text()
                        text02 = self.Text02.text()
                        text10 = self.Text10.text()
                        text11 = self.Text11.text()
                        text12 = self.Text12.text()
                        text20 = self.Text20.text()
                        text21 = self.Text21.text()
                        text22 = self.Text22.text()

                        if text02 == text12 and text12 == text22: #v1
                            if not text02 == "":
                                textvictoria = "Victoria de: " + text02
                                self.BotonIniciar.setText("INICIAR")
                                self.segundoPlano.stop()
                                #print(textvictoria)
                                msg = QMessageBox()
                                msg.setText(textvictoria)
                                msg.setWindowTitle("Victoria")
                                msg.setStandardButtons(QMessageBox.Ok)
                                msg.exec()
                        elif text01 == text11 and text11 == text21: #v2
                            if not text01 == "":
                                textvictoria = "Victoria de: " + text01
                                self.BotonIniciar.setText("INICIAR")
                                self.segundoPlano.stop()
                                # print(textvictoria)
                                msg = QMessageBox()
                                msg.setText(textvictoria)
                                msg.setWindowTitle("Victoria")
                                msg.setStandardButtons(QMessageBox.Ok)
                                msg.exec()
                        elif text00 == text10 and text10 == text20: #v3
                            if not text00 == "":
                                textvictoria = "Victoria de: " + text00
                                self.BotonIniciar.setText("INICIAR")
                                self.segundoPlano.stop()
                                # print(textvictoria)
                                msg = QMessageBox()
                                msg.setText(textvictoria)
                                msg.setWindowTitle("Victoria")
                                msg.setStandardButtons(QMessageBox.Ok)
                                msg.exec()
                        elif text02 == text01 and text01 == text00: #v4
                            if not text02 == "":
                                textvictoria = "Victoria de: " + text02
                                self.BotonIniciar.setText("INICIAR")
                                self.segundoPlano.stop()
                                # print(textvictoria)
                                msg = QMessageBox()
                                msg.setText(textvictoria)
                                msg.setWindowTitle("Victoria")
                                msg.setStandardButtons(QMessageBox.Ok)
                                msg.exec()
                        elif text12 == text11 and text11 == text10: #v5
                            if not text12 == "":
                                textvictoria = "Victoria de: " + text12
                                self.BotonIniciar.setText("INICIAR")
                                self.segundoPlano.stop()
                                # print(textvictoria)
                                msg = QMessageBox()
                                msg.setText(textvictoria)
                                msg.setWindowTitle("Victoria")
                                msg.setStandardButtons(QMessageBox.Ok)
                                msg.exec()
                        elif text22 == text21 and text21 == text20: #v6
                            if not text22 == "":
                                textvictoria = "Victoria de: " + text22
                                self.BotonIniciar.setText("INICIAR")
                                self.segundoPlano.stop()
                                # print(textvictoria)
                                msg = QMessageBox()
                                msg.setText(textvictoria)
                                msg.setWindowTitle("Victoria")
                                msg.setStandardButtons(QMessageBox.Ok)
                                msg.exec()
                        elif text02 == text11 and text11 == text20: #v7
                            if not text02 == "":
                                textvictoria = "Victoria de: " + text02
                                self.BotonIniciar.setText("INICIAR")
                                self.segundoPlano.stop()
                                # print(textvictoria)
                                msg = QMessageBox()
                                msg.setText(textvictoria)
                                msg.setWindowTitle("Victoria")
                                msg.setStandardButtons(QMessageBox.Ok)
                                msg.exec()
                        elif text22 == text11 and text11 == text00: #v8
                            if not text22 == "":
                                textvictoria = "Victoria de: " + text22
                                self.BotonIniciar.setText("INICIAR")
                                self.segundoPlano.stop()
                                # print(textvictoria)
                                msg = QMessageBox()
                                msg.setText(textvictoria)
                                msg.setWindowTitle("Victoria")
                                msg.setStandardButtons(QMessageBox.Ok)
                                msg.exec()

                        if not coordenadas == "":
                            if coordenadas == "seleccionar":
                                if self.turno % 2 == 0:
                                    self.respuesta = "X"
                                else:
                                    self.respuesta = "O"

                                lugar = "Text" + self.TextCooX.text() + self.TextCooY.text()

                                txt = self.findChild(QtWidgets.QLineEdit, lugar)

                                if txt.text() == "":
                                    txt.setText(self.respuesta)

                                    self.turno = self.turno + 1

    #                                if self.TextCooX.Text() == "0" and self.TextCooY.Text() == "0":
    #                                    self.Text00.setText(self.respuesta)
    #                                elif self.TextCooX.Text() == "0" and self.TextCooY.Text() == "1":
    #                                    self.Text01.setText(self.respuesta)
    #                                elif self.TextCooX.Text() == "0" and self.TextCooY.Text() == "2":
    #                                    self.Text02.setText(self.respuesta)
    #                                elif self.TextCooX.Text() == "1" and self.TextCooY.Text() == "0":
    #                                    self.Text10.setText(self.respuesta)
    #                                elif self.TextCooX.Text() == "1" and self.TextCooY.Text() == "1":
    #                                    self.Text11.setText(self.respuesta)
    #                                elif self.TextCooX.Text() == "1" and self.TextCooY.Text() == "2":
    #                                    self.Text12.setText(self.respuesta)
    #                                elif self.TextCooX.Text() == "2" and self.TextCooY.Text() == "0":
    #                                    self.Text20.setText(self.respuesta)
    #                                elif self.TextCooX.Text() == "2" and self.TextCooY.Text() == "1":
    #                                    self.Text21.setText(self.respuesta)
    #                                else:
    #                                    self.Text22.setText(self.respuesta)
                                    if self.turno == 9:
                                        self.BotonIniciar.setText("INICIAR")
                                        self.segundoPlano.stop()

                            else:
                                if not coordenadas == "seleccionar":
                                    datos = coordenadas.split(",")

                                    self.TextCooX.setText(datos[0])
                                    self.TextCooY.setText(datos[1])
                                    #print(datos)

                                    self.Text00.setStyleSheet("")
                                    self.Text01.setStyleSheet("")
                                    self.Text02.setStyleSheet("")
                                    self.Text10.setStyleSheet("")
                                    self.Text11.setStyleSheet("")
                                    self.Text12.setStyleSheet("")
                                    self.Text20.setStyleSheet("")
                                    self.Text21.setStyleSheet("")
                                    self.Text22.setStyleSheet("")

                                    lugar = "Text" + self.TextCooX.text() + self.TextCooY.text()

                                    txt = self.findChild(QtWidgets.QLineEdit, lugar)

                                    txt.setStyleSheet("background-color: rgb(127,255,212);")
        except Exception as error:
            print(error)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())