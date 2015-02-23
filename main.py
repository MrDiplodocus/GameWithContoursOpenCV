#!/usr/bin/python
# -*- coding: utf_8 -*-

import numpy as np
import cv
import cv2
from PyQt4 import QtCore, QtGui
import filters
import ui_mainwindow

class MyWindow(QtGui.QMainWindow, ui_mainwindow.Ui_MainWindow):
    pathOriginalFile = ''
    imageContours = ''
    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.pShowOriginal.clicked.connect(self.showOriginalImage)
        self.actionOpen.triggered.connect(self.showDialog)
        self.chCanny.clicked.connect(self.enableCanny)
        self.checkBox.clicked.connect(self.enableApprox)
        self.radioButton.clicked.connect(self.enableKuwahara)
        self.radioButton_2.clicked.connect(self.enableGaussian)
        self.radioButton_3.clicked.connect(self.enableMedian)
        self.radioButton_4.clicked.connect(self.enableBilateral)
        self.horizontalSlider.valueChanged.connect(self.drawContours)
        self.horizontalSlider_2.valueChanged.connect(self.drawContours)

    def showOriginalImage(self):
        img = cv2.imread(self.pathOriginalFile, 1)
        cv2.imshow("Original", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def showDialog(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open image', '/*.jpg')
        file = open(filename)
        self.pathOriginalFile = str(filename)
        self.imageContours = cv2.imread(self.pathOriginalFile)
        cv2.imshow("Contours", self.imageContours)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        # scene = QtGui.QGraphicsScene()
        # scene.addPixmap(filename)
        # self.graphicsView.setScene(scene)
        # self.graphicsView.show()

    def enableCanny(self):
        self.horizontalSlider_3.setEnabled(self.chCanny.isChecked())
        self.horizontalSlider_4.setEnabled(self.chCanny.isChecked())
        self.horizontalSlider_5.setEnabled(self.chCanny.isChecked())
        self.chL2Gradient.setEnabled(self.chCanny.isChecked())

    def enableKuwahara(self):
        self.horizontalSlider_6.setEnabled(True)
        self.horizontalSlider_7.setEnabled(False)
        self.horizontalSlider_8.setEnabled(False)
        self.horizontalSlider_9.setEnabled(False)
        self.horizontalSlider_10.setEnabled(False)
        self.horizontalSlider_11.setEnabled(False)

    def enableGaussian(self):
        self.horizontalSlider_6.setEnabled(True)
        self.horizontalSlider_7.setEnabled(True)
        self.horizontalSlider_8.setEnabled(True)
        self.horizontalSlider_9.setEnabled(False)
        self.horizontalSlider_10.setEnabled(False)
        self.horizontalSlider_11.setEnabled(False)

    def enableMedian(self):
        self.horizontalSlider_6.setEnabled(True)
        self.horizontalSlider_7.setEnabled(False)
        self.horizontalSlider_8.setEnabled(False)
        self.horizontalSlider_9.setEnabled(False)
        self.horizontalSlider_10.setEnabled(False)
        self.horizontalSlider_11.setEnabled(False)

    def enableBilateral(self):
        self.horizontalSlider_6.setEnabled(False)
        self.horizontalSlider_7.setEnabled(False)
        self.horizontalSlider_8.setEnabled(False)
        self.horizontalSlider_9.setEnabled(True)
        self.horizontalSlider_10.setEnabled(True)
        self.horizontalSlider_11.setEnabled(True)

    def enableApprox(self):
        self.doubleSpinBox.setEnabled(self.checkBox.isChecked())

    def drawContours(self):
        self.imageContours = cv2.imread(self.pathOriginalFile, 1)
        gray = cv2.cvtColor(self.imageContours, cv2.COLOR_BGR2GRAY)
        #edges = cv2.Canny(gray, self.horizontalSlider.value(), self.horizontalSlider_2.value())
        ret, thresh = cv2.threshold(gray, self.horizontalSlider.value(), self.horizontalSlider_2.value(), 0)
        contours, hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(self.imageContours, contours, -1, (0,0,255), 2)
        cv2.imshow("Contours", self.imageContours)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())