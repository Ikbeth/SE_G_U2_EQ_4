import sys
import serial as conecta
from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "P_6_GUI_Python_Arduino.ui"  # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_accion.clicked.connect(self.accion)
        self.arduino = None

        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.control)

    # Área de los Slots
    def accion(self):
        try:
            txt_boton = self.btn_accion.text()
            if txt_boton == "CONECTAR":
                self.txt_estado.setText("CONECTADO")
                self.btn_accion.setText("DESCONECTAR")

                puerto = "COM" + self.txt_puerto.text()

                self.arduino = conecta.Serial(puerto, baudrate=9600, timeout=1)
                self.segundoPlano.start(100)

            elif txt_boton == "DESCONECTAR":
                self.txt_estado.setText("DESCONECTADO")
                self.btn_accion.setText("RECONECTAR")

                self.arduino.close()
                self.segundoPlano.stop()
            else: #RECONECTAR
                self.txt_estado.setText("RECONECTADO")
                self.btn_accion.setText("DESCONECTAR")

                self.arduino.open()
                self.segundoPlano.start(100)

        except Exception as error:
            print(error)

    def control(self):
        if not self.arduino == None:
            if self.arduino.isOpen():
                    #leer
                variable = self.arduino.readline().decode()
                variable = variable.replace("\n","")
                variable = variable.replace("\r","")

            #self.arduino.isOpen()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

##ejercicio experimentacion:
## generar prog en arduino que imprima el valor dde la ariable e incrementa en 1 en medio seg