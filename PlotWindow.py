from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib
import numpy as np

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

from plotwall import plotwall

class PlotWindow(QtWidgets.QFrame):
    def __init__(self, parent=None):
        super(PlotWindow, self).__init__(parent)

        self.figure = Figure(facecolor='black')
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.image = None
        self.ax = None
        self.setWindowTitle('SOFT Camera Calibration')
        self.wall = None
        self.detpos = None
        self.detdir = None
        self.visang = None
        self.tiltAngle = None

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        self.setLayout(layout)

    def drawSafe(self):
        try:
            self.canvas.draw()
        except RuntimeError as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(e.strerror)
            msg.setWindowTitle('Runtime Error')
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

    def gen(self, fig):
        fig.clear()
        ax = fig.add_subplot(111)
        pixelscale = 1

        if self.wall is not None:
            #distance = np.abs(np.dot(self.detpos, self.detdir))
            #L = np.sqrt(2) * distance * np.tan(self.visang / 2)
            #pixelscale = L / 2
            pixelscale = np.tan(self.visang / 2) / 2
            
        if self.image is not None:
            h = self.image.shape[0]
            w = self.image.shape[1]

            extent = []
            if h >= w:
                extent = [-(w/h)*pixelscale,(w/h)*pixelscale,-pixelscale,pixelscale]
            else:
                extent = [-pixelscale,pixelscale,-(h/w)*pixelscale,(h/w)*pixelscale]

            ax.imshow(self.image, extent=extent)

        if self.wall is not None:
            plotwall(ax, self.wall, self.detpos, self.detdir, degreesStart=[-30, 210], degreesEnd=[-29,211], tiltAngle=self.tiltAngle)
            plotwall(ax, self.wall, self.detpos, self.detdir, degreesStart=[190], degreesEnd=[350], rlim=0.46, spacing=5, tiltAngle=self.tiltAngle)
            plotwall(ax, self.wall, self.detpos, self.detdir, degreesStart=[190], degreesEnd=[350], zuplim=-0.4, spacing=3, tiltAngle=self.tiltAngle)

            ax.set_xlim([-pixelscale,pixelscale])
            ax.set_ylim([-pixelscale,pixelscale])

        fig.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
        ax.set_axis_off()

        return ax

    def plot(self):
        self.ax = self.gen(self.figure)
        self.drawSafe()

    def setImage(self, image):
        self.image = image
        self.plot()

    def setWall(self, wall, detpos, detdir, visang, tiltAngle):
        self.wall = wall
        self.detpos = detpos
        self.detdir = detdir
        self.visang = visang
        self.tiltAngle = tiltAngle

        self.plot()

