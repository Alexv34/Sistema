from doctest import DONT_ACCEPT_TRUE_FOR_1
import sys
import numpy as np
from ui_grafico import *
from PySide2 import QtCore,QtWidgets,QtGui
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from pylab import *
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class MiApp(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow() 
        self.ui.setupUi(self)


        self.grafica = Canvas_grafica()

        self.ui.grafica.addWidget(self.grafica)

        self.ui.insetar.clicked.connect(self.agregar)
#-------------------datos
    def agregar(self):
        dato1=int(self.ui.valor1.value())
        dato2=int(self.ui.valor2.value())
        return dato1,dato2
#----------Graficos
class Canvas_grafica(FigureCanvas,QWidget,Ui_MainWindow):
    def __init__(self, parent=None):    
        self.fig , self.ax = plt.subplots(1, dpi=100, figsize=(5, 5), 
            sharey=True, facecolor='white')
        super().__init__(self.fig) 



        plt.xlim(-1,10)
        plt.ylim(-1,10)
        plt.figure(1)
        fig = plt.gcf()
        DPI = fig.get_dpi()
        fig.set_size_inches(6, 4)
        x,y=np.linspace(0,10),np.linspace(0,10)

        y=4
        x=3

        plt.plot(x,label='iluminacion',marker='*',linestyle='None',markersize=10)
        plt.plot(y,label='Toma corriente',marker='s',linestyle='None',markersize=10)
        plt.legend(loc="upper left")
        plt.plot(x, y)
        plt.title('Cableado')
        plt.xlabel('X')
        plt.ylabel('Y')
        # ------------------------------- marco cuadrado
        self.ax.add_patch(
        patches.Rectangle(
            (0, 0),
            x,
            y,
            edgecolor = 'green',
            fill=False      
        ) )

if __name__ == "__main__":
     app = QApplication(sys.argv)
     mi_app = MiApp()
     mi_app.show()
     sys.exit(app.exec_())  