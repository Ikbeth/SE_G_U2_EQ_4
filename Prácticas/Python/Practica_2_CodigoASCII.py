import sys
from time import sleep
import serial as conecta

from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "Practica_2_CodigoASCII.ui"  # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

#OPCION 3 SERIALIZACION

#E + l = +

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_accion.clicked.connect(self.accion)
        self.arduino = None

        self.segundoPlano = QtCore.QTimer()
        self.envioDatos = QtCore.QTimer()

        self.btn_Enviar.clicked.connect(self.enviar)
        #self.btn_controlled.setEnabled(False)

    # Área de los Slots
    def enviar(self):
        if not self.arduino == None:
            if self.arduino.isOpen():
                cadena = self.txt_cadena.text()
                valA = []
                for i in cadena:
                    valA.append(ord(i))

                for j in range(len(valA)):
                    self.arduino.write(str(valA[j]).encode())
                    print(cadena[j], " = ", valA[j])
                    sleep(4)

                self.txt_cadena.setText("")
                self.arduino.write("0".encode())

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


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())