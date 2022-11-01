# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Import the core and GUI elements of Qt

import qrcode  
from qrLib import *
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import * 
from PIL.ImageQt import ImageQt

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

def uret():
    _lineBilgi=ui.lineEdit.text()
    qr_img = qrcode.make(_lineBilgi)
    
    qimage = ImageQt(qr_img)
    pixmap = QtGui.QPixmap.fromImage(qimage)
    ui.qrImage.setPixmap(QtGui.QPixmap(pixmap))
   
_lineBilgi=" "
    
ui.pushButton.clicked.connect(uret)
   
sys.exit(app.exec_())