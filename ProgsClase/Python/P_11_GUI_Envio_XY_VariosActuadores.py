import sys
import serial as conecta

from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "P_11_GUI_Envio_XY_VariosSensores.ui"  # Nombre del archivo aquí.

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
        self.segundoPlano.timeout.connect(self.control)

        self.btn_controlled.clicked.connect(self.control_led)
        #self.btn_controlled.setEnabled(False)

    # Área de los Slots
    def control_led(self):
        if not self.arduino == None:
            if self.arduino.isOpen():
                actuador1 = 100
                actuador2 = 56
                actuador3 = 360

                actuador1 = self.Validarlongitud(actuador1)
                actuador2 = self.Validarlongitud(actuador2)
                actuador3 = self.Validarlongitud(actuador3)

                cadenaSerealizda = "E" + str(actuador1) + "R" + str(actuador2) + "R"  + str(actuador3) + "C"
                print(cadenaSerealizda)

                self.arduino.write(cadenaSerealizda.encode())

    def Validarlongitud(self, valSensor):
        cadenaModificada = valSensor
        return cadenaModificada

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



    def control(self):
        try:
            if not self.arduino == None:
                if self.arduino.isOpen():
                    #leer
                    if self.arduino.inWaiting():
                        variable = self.arduino.readline().decode()
                        variable = variable.replace("\r","")
                        variable = variable.replace("\n","")
                        #print(variable)
                        ver = self.cbx_visualizar.isChecked()
                        archivo = open("../Archivos/Datos_11.txt", "a")
                        archivo.write(variable + "\n")
                        if not variable == "":
                            if ver:
                                self.lw_datos.addItem(variable)
                                self.lw_datos.setCurrentRow(self.lw_datos.count()-1)
                        archivo.close()
        except Exception as error:
            print(error)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

