# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(481, 376)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 111, 28))
        self.label.setObjectName("label")
        self.tbEquilibrium = QtWidgets.QLineEdit(self.centralwidget)
        self.tbEquilibrium.setGeometry(QtCore.QRect(120, 20, 271, 28))
        self.tbEquilibrium.setObjectName("tbEquilibrium")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 91, 28))
        self.label_2.setObjectName("label_2")
        self.tbImage = QtWidgets.QLineEdit(self.centralwidget)
        self.tbImage.setGeometry(QtCore.QRect(120, 50, 271, 28))
        self.tbImage.setObjectName("tbImage")
        self.btnBrowseEq = QtWidgets.QPushButton(self.centralwidget)
        self.btnBrowseEq.setGeometry(QtCore.QRect(390, 20, 84, 28))
        self.btnBrowseEq.setObjectName("btnBrowseEq")
        self.btnBrowseImage = QtWidgets.QPushButton(self.centralwidget)
        self.btnBrowseImage.setGeometry(QtCore.QRect(390, 50, 84, 28))
        self.btnBrowseImage.setObjectName("btnBrowseImage")
        self.gbDetector = QtWidgets.QGroupBox(self.centralwidget)
        self.gbDetector.setGeometry(QtCore.QRect(10, 100, 461, 221))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.gbDetector.setFont(font)
        self.gbDetector.setObjectName("gbDetector")
        self.label_3 = QtWidgets.QLabel(self.gbDetector)
        self.label_3.setGeometry(QtCore.QRect(250, 30, 21, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.gbDetector)
        self.label_4.setGeometry(QtCore.QRect(330, 30, 21, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.gbDetector)
        self.label_5.setGeometry(QtCore.QRect(410, 30, 21, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.tbPosX = QtWidgets.QLineEdit(self.gbDetector)
        self.tbPosX.setGeometry(QtCore.QRect(220, 50, 71, 28))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.tbPosX.setFont(font)
        self.tbPosX.setObjectName("tbPosX")
        self.tbPosY = QtWidgets.QLineEdit(self.gbDetector)
        self.tbPosY.setGeometry(QtCore.QRect(300, 50, 71, 28))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.tbPosY.setFont(font)
        self.tbPosY.setObjectName("tbPosY")
        self.tbPosZ = QtWidgets.QLineEdit(self.gbDetector)
        self.tbPosZ.setGeometry(QtCore.QRect(380, 50, 71, 28))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.tbPosZ.setFont(font)
        self.tbPosZ.setObjectName("tbPosZ")
        self.tbDirX = QtWidgets.QLineEdit(self.gbDetector)
        self.tbDirX.setGeometry(QtCore.QRect(220, 80, 71, 28))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.tbDirX.setFont(font)
        self.tbDirX.setObjectName("tbDirX")
        self.tbDirZ = QtWidgets.QLineEdit(self.gbDetector)
        self.tbDirZ.setGeometry(QtCore.QRect(380, 80, 71, 28))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.tbDirZ.setFont(font)
        self.tbDirZ.setObjectName("tbDirZ")
        self.tbDirY = QtWidgets.QLineEdit(self.gbDetector)
        self.tbDirY.setGeometry(QtCore.QRect(300, 80, 71, 28))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.tbDirY.setFont(font)
        self.tbDirY.setObjectName("tbDirY")
        self.label_6 = QtWidgets.QLabel(self.gbDetector)
        self.label_6.setGeometry(QtCore.QRect(10, 50, 131, 28))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.gbDetector)
        self.label_7.setGeometry(QtCore.QRect(10, 80, 191, 28))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.gbDetector)
        self.label_8.setGeometry(QtCore.QRect(10, 110, 141, 28))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.tbVisang = QtWidgets.QLineEdit(self.gbDetector)
        self.tbVisang.setGeometry(QtCore.QRect(220, 110, 151, 28))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.tbVisang.setFont(font)
        self.tbVisang.setObjectName("tbVisang")
        self.label_9 = QtWidgets.QLabel(self.gbDetector)
        self.label_9.setGeometry(QtCore.QRect(380, 110, 63, 28))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.gbDetector)
        self.label_10.setGeometry(QtCore.QRect(10, 140, 151, 28))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.tbTilt = QtWidgets.QLineEdit(self.gbDetector)
        self.tbTilt.setGeometry(QtCore.QRect(220, 140, 151, 28))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.tbTilt.setFont(font)
        self.tbTilt.setObjectName("tbTilt")
        self.label_11 = QtWidgets.QLabel(self.gbDetector)
        self.label_11.setGeometry(QtCore.QRect(380, 140, 63, 28))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.btnRedraw = QtWidgets.QPushButton(self.gbDetector)
        self.btnRedraw.setGeometry(QtCore.QRect(370, 180, 84, 28))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btnRedraw.setFont(font)
        self.btnRedraw.setObjectName("btnRedraw")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 481, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Equilibrium file:"))
        self.label_2.setText(_translate("MainWindow", "Image file:"))
        self.btnBrowseEq.setText(_translate("MainWindow", "Browse..."))
        self.btnBrowseImage.setText(_translate("MainWindow", "Browse..."))
        self.gbDetector.setTitle(_translate("MainWindow", "Detector properties"))
        self.label_3.setText(_translate("MainWindow", "X"))
        self.label_4.setText(_translate("MainWindow", "Y"))
        self.label_5.setText(_translate("MainWindow", "Z"))
        self.tbPosX.setText(_translate("MainWindow", "0"))
        self.tbPosY.setText(_translate("MainWindow", "0"))
        self.tbPosZ.setText(_translate("MainWindow", "0"))
        self.tbDirX.setText(_translate("MainWindow", "0"))
        self.tbDirZ.setText(_translate("MainWindow", "0"))
        self.tbDirY.setText(_translate("MainWindow", "1"))
        self.label_6.setText(_translate("MainWindow", "Position:"))
        self.label_7.setText(_translate("MainWindow", "Viewing direction:"))
        self.label_8.setText(_translate("MainWindow", "Vision angle:"))
        self.tbVisang.setText(_translate("MainWindow", "1"))
        self.label_9.setText(_translate("MainWindow", "rad"))
        self.label_10.setText(_translate("MainWindow", "CW tilt:"))
        self.tbTilt.setText(_translate("MainWindow", "0"))
        self.label_11.setText(_translate("MainWindow", "rad"))
        self.btnRedraw.setText(_translate("MainWindow", "Redraw"))

