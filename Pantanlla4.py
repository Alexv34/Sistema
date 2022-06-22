import sys
from PySide2 import QtWidgets
from ui_Pantanlla4 import *


class MyApp(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.calcular.clicked.connect(self.calculos)
    def calculos(self):
        Tg1=float(self.TG.value())
        LL1=float(self.LL1P.value())
        Tc=float(self.TC.value())
        Ze=float(self.dat_z.value())
        resultado="La cañeria del Tablero"+str(Tg1-Ze)+"La cañeria del Tablero"+str(Tc-Ze)+"La cañeria del Tablero"+str(LL1-Ze)
        self.textBrowser.setText(resultado)



if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())