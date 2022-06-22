# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Pantanlla4eJupfH.ui'
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
        self.frame_2.setGeometry(QRect(170, 10, 511, 521))
        self.frame_2.setStyleSheet(u"background-color: rgb(85, 255, 255);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.TC = QLineEdit(self.frame_2)
        self.TC.setObjectName(u"TC")
        self.TC.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.TC, 5, 1, 1, 1)

        self.TG = QLineEdit(self.frame_2)
        self.TG.setObjectName(u"TG")
        self.TG.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.TG, 3, 1, 1, 1)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

        self.LL1P = QLineEdit(self.frame_2)
        self.LL1P.setObjectName(u"LL1P")
        self.LL1P.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.LL1P, 3, 3, 1, 1)

        self.dat_z = QLineEdit(self.frame_2)
        self.dat_z.setObjectName(u"dat_z")
        self.dat_z.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.dat_z, 5, 3, 1, 1)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 5, 2, 1, 1)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 2, 1, 1)

        self.calcular = QPushButton(self.frame_2)
        self.calcular.setObjectName(u"calcular")
        self.calcular.setStyleSheet(u"background-color: rgb(247, 255, 161);")

        self.gridLayout.addWidget(self.calcular, 6, 2, 1, 1)

        self.textBrowser = QTextBrowser(self.frame_2)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setStyleSheet(u"background-color: rgb(203, 203, 203);")

        self.gridLayout.addWidget(self.textBrowser, 8, 0, 1, 4)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 4)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(10, 10, 151, 521))
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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TG", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"TC", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"LL1P", None))
        self.calcular.setText(QCoreApplication.translate("MainWindow", u"Calcular", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Datos de Calculo", None))
        self.pantalla1.setText(QCoreApplication.translate("MainWindow", u"pantalla1", None))
        self.pantalla2.setText(QCoreApplication.translate("MainWindow", u"pantalla2", None))
        self.pantalla3.setText(QCoreApplication.translate("MainWindow", u"pantalla3", None))
        self.pantalla4.setText(QCoreApplication.translate("MainWindow", u"pantalla4", None))
        self.pantalla5.setText(QCoreApplication.translate("MainWindow", u"pantalla5", None))
        self.pantalla6.setText(QCoreApplication.translate("MainWindow", u"pantalla6", None))
        self.pantalla7.setText(QCoreApplication.translate("MainWindow", u"pantalla7", None))
    # retranslateUi

