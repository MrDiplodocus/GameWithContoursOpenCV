#!/usr/bin/python
# -*- coding: utf_8 -*-

import numpy as np
import cv2
from PyQt4 import QtCore, QtGui
import filters
import ui_mainwindow

class MyWindow(QtGui.QMainWindow, ui_mainwindow.Ui_MainWindow):
    pathOriginalFile = ''
    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.pShowOriginal.clicked.connect(self.showOriginalImage)
        self.actionOpen.triggered.connect(self.showDialog)

    def showOriginalImage(self):
        img = cv2.imread(self.pathOriginalFile, 1)
        cv2.imshow("Original", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def showDialog(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open image', '/*.jpg')
        file = open(filename)
        self.pathOriginalFile = str(filename)
        #scene = QtGui.QGraphicsScene()
        #scene.addPixmap(filename)
        #self.graphicsView.setScene(scene)
        #self.graphicsView.show()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())