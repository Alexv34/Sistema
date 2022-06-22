# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'graficoivxCyr.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(708, 560)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(0, 170, 255);\n"
"background-color: rgb(188, 190, 189);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(170, 10, 511, 111))
        self.frame_2.setStyleSheet(u"background-color: rgb(85, 255, 255);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 4, 0, 1, 1)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.gridLayout_2.addWidget(self.label, 1, 2, 1, 1)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)

        self.insetar = QPushButton(self.frame_2)
        self.insetar.setObjectName(u"insetar")

        self.gridLayout_2.addWidget(self.insetar, 2, 3, 1, 1)

        self.graficar = QPushButton(self.frame_2)
        self.graficar.setObjectName(u"graficar")

        self.gridLayout_2.addWidget(self.graficar, 4, 3, 1, 1)

        self.valor1 = QLineEdit(self.frame_2)
        self.valor1.setObjectName(u"valor1")
        self.valor1.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.valor1, 2, 1, 1, 1)

        self.valor4 = QLineEdit(self.frame_2)
        self.valor4.setObjectName(u"valor4")
        self.valor4.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.valor4, 4, 2, 1, 1)

        self.valor3 = QLineEdit(self.frame_2)
        self.valor3.setObjectName(u"valor3")
        self.valor3.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.valor3, 4, 1, 1, 1)

        self.valor2 = QLineEdit(self.frame_2)
        self.valor2.setObjectName(u"valor2")
        self.valor2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.valor2, 2, 2, 1, 1)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(170, 130, 511, 381))
        self.frame_3.setStyleSheet(u"\n"
"background-color: rgb(85, 255, 255);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.grafica = QVBoxLayout()
        self.grafica.setObjectName(u"grafica")

        self.gridLayout.addLayout(self.grafica, 0, 0, 1, 1)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(10, 10, 151, 501))
        self.frame_4.setStyleSheet(u"background-color: rgb(85, 255, 127);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pantalla1 = QPushButton(self.frame_4)
        self.pantalla1.setObjectName(u"pantalla1")

        self.verticalLayout_2.addWidget(self.pantalla1)

        self.pantalla2 = QPushButton(self.frame_4)
        self.pantalla2.setObjectName(u"pantalla2")

        self.verticalLayout_2.addWidget(self.pantalla2)

        self.pantalla3 = QPushButton(self.frame_4)
        self.pantalla3.setObjectName(u"pantalla3")

        self.verticalLayout_2.addWidget(self.pantalla3)

        self.pantalla4 = QPushButton(self.frame_4)
        self.pantalla4.setObjectName(u"pantalla4")

        self.verticalLayout_2.addWidget(self.pantalla4)

        self.pantalla5 = QPushButton(self.frame_4)
        self.pantalla5.setObjectName(u"pantalla5")

        self.verticalLayout_2.addWidget(self.pantalla5)

        self.pantalla6 = QPushButton(self.frame_4)
        self.pantalla6.setObjectName(u"pantalla6")

        self.verticalLayout_2.addWidget(self.pantalla6)

        self.pantalla7 = QPushButton(self.frame_4)
        self.pantalla7.setObjectName(u"pantalla7")

        self.verticalLayout_2.addWidget(self.pantalla7)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sistema electrico", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"objetos", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Datos de la Grafica", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Cuadro", None))
        self.insetar.setText(QCoreApplication.translate("MainWindow", u"Insertar", None))
        self.graficar.setText(QCoreApplication.translate("MainWindow", u"Graficar", None))
        self.pantalla1.setText(QCoreApplication.translate("MainWindow", u"pantalla1", None))
        self.pantalla2.setText(QCoreApplication.translate("MainWindow", u"pantalla2", None))
        self.pantalla3.setText(QCoreApplication.translate("MainWindow", u"pantalla3", None))
        self.pantalla4.setText(QCoreApplication.translate("MainWindow", u"pantalla4", None))
        self.pantalla5.setText(QCoreApplication.translate("MainWindow", u"pantalla5", None))
        self.pantalla6.setText(QCoreApplication.translate("MainWindow", u"pantalla6", None))
        self.pantalla7.setText(QCoreApplication.translate("MainWindow", u"pantalla7", None))
    # retranslateUi

