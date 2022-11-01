# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qrLib.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(458, 190)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 50, 47, 13))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(90, 50, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.qrImage = QtWidgets.QLabel(self.centralwidget)
        self.qrImage.setGeometry(QtCore.QRect(310, 20, 111, 111))
        self.qrImage.setText("")
        self.qrImage.setPixmap(QtGui.QPixmap("../Capture.PNG"))
        self.qrImage.setScaledContents(True)
        self.qrImage.setObjectName("qrImage")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 80, 111, 31))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(310, 150, 141, 20))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Qr Generator"))
        self.label.setText(_translate("MainWindow", "QR Bilgisi"))
        self.pushButton.setText(_translate("MainWindow", "Qr Üret"))
        self.label_2.setText(_translate("MainWindow", "https://github.com/MrHkk61"))




