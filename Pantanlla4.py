from multiprocessing.sharedctypes import Value
import sys
from PySide2 import QtWidgets
from numpy import double
from ui_Pantanlla4 import *


class MyApp(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.calcular.clicked.connect(self.calculos)
    def calculos(self):
        Tg1=double(self.TG.text())
        LL1=double(self.LL1P.text())
        Tc=double(self.TC.text())
        Ze=double(self.dat_z.text())
        resultado="La cañeria del Tablero General: "+str(Tg1-Ze)+"m"+"\nLa cañeria de Llave: "+str(Tc-Ze)+"m"+"\nLa cañeria Tomacorriente: "+str(LL1-Ze)+"m"
        self.textBrowser.setText(resultado)



if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
