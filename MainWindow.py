
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from ui import main_design
import sys
import numpy as np
import numpy.linalg
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import scipy.io
import h5py

from PlotWindow import PlotWindow

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = main_design.Ui_MainWindow()
        self.ui.setupUi(self)

        self.wall = None
        self.image = None
        self.plotWindow = PlotWindow()
        self.ui.gbDetector.setEnabled(False)

        self.bindEvents()

    def bindEvents(self):
        self.ui.btnBrowseEq.clicked.connect(self.openEquilibrium)
        self.ui.btnBrowseImage.clicked.connect(self.openImage)
        self.ui.btnRedraw.clicked.connect(self.updateWall)

    def closeEvent(self):
        self.exit()

    def exit(self):
        self.plotWindow.close()
        self.close()

    def openEquilibrium(self):
        filename, _ = QFileDialog.getOpenFileName(parent=self, caption="Open SOFT magnetic equilibrium", filter="SOFT Equilibrium Data (*.h5 *.mat)")

        if filename:
            self.ui.tbEquilibrium.setText(filename)
            if filename.endswith('.mat'):
                matfile = scipy.io.loadmat(filename)
                self.wall = matfile['wall']
            elif filename.endswith('.h5') or filename.endswith('.hdf5'):
                hfile = h5py.File(filename, 'r')
                self.wall = list(hfile['wall'])
                hfile.close()

            self.ui.gbDetector.setEnabled(True)
            self.updateWall()
        
    def openImage(self):
        filename, _ = QFileDialog.getOpenFileName(parent=self, caption="Open SOFT magnetic equilibrium", filter="Image (*.jpeg *jpg *.png)")

        if filename:
            self.ui.tbImage.setText(filename)
            self.image = mpimg.imread(filename)
            
            if not self.plotWindow.isVisible():
                self.plotWindow.show()

            self.plotWindow.setImage(self.image)

    def updateWall(self):
        if not self.plotWindow.isVisible():
            self.plotWindow.show()

        try:
            detpos = np.array([float(self.ui.tbPosX.text()), float(self.ui.tbPosY.text()), float(self.ui.tbPosZ.text())])
            detdir = np.array([float(self.ui.tbDirX.text()), float(self.ui.tbDirY.text()), float(self.ui.tbDirZ.text())])
            detdir = detdir / np.linalg.norm(detdir)
            visang = float(self.ui.tbVisang.text())
            tiltAngle = float(self.ui.tbTilt.text())
            self.plotWindow.setWall(self.wall, detpos, detdir, visang, tiltAngle)
        except ValueError as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(e.strerror)
            msg.setWindowTitle('Runtime Error')
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

