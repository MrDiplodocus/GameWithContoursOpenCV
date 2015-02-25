#!/usr/bin/python
# -*- coding: utf_8 -*-
from cv2 import drawContours

import numpy as np
import cv
import cv2
from PyQt4 import QtCore, QtGui
from special_methods import *
import filters
import ui_form



class MyWindow(QtGui.QMainWindow, ui_form.Ui_MainWindow):
    pathOriginalFile = ''
    imageContours = ''
    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.pShowOriginal.clicked.connect(self.showOriginalImage)
        self.actionOpen.triggered.connect(self.showDialog)
        #self.chCanny.clicked.connect(self.enableCanny)
        self.checkBox.clicked.connect(self.enableApprox)
        #self.radioButton.clicked.connect(self.enableKuwahara)
        self.radioButton_2.clicked.connect(self.enableGaussian)
        self.radioButton_3.clicked.connect(self.enableMedian)
        self.radioButton_4.clicked.connect(self.enableBilateral)
        self.horizontalSlider.valueChanged.connect(self.drawContours)
        self.horizontalSlider_2.valueChanged.connect(self.drawContours)
        self.comboBox.activated.connect(self.drawContours)
        self.comboBox_2.activated.connect(self.drawContours)
        self.checkBox.clicked.connect(self.drawContours)
        self.doubleSpinBox.valueChanged.connect(self.drawContours)
        self.checkBox_2.clicked.connect(self.drawContours)
        self.radioButton_3.clicked.connect(self.drawContours)
        self.horizontalSlider_6.valueChanged.connect(self.drawContours)
        self.radioButton_2.clicked.connect(self.drawContours)
        self.horizontalSlider_7.valueChanged.connect(self.drawContours)
        self.horizontalSlider_8.valueChanged.connect(self.drawContours)
        self.radioButton_4.clicked.connect(self.drawContours)
        self.horizontalSlider_9.valueChanged.connect(self.drawContours)
        self.horizontalSlider_10.valueChanged.connect(self.drawContours)
        self.horizontalSlider_11.valueChanged.connect(self.drawContours)


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
        self.checkBox_2.setEnabled(self.checkBox.isChecked())

    def drawContours(self):
        self.imageContours = cv2.imread(self.pathOriginalFile, 1)
        gray = cv2.cvtColor(self.imageContours, cv2.COLOR_BGR2GRAY)

        if self.radioButton_3.isChecked():
            gray = filters.Median(gray, self.horizontalSlider_6.value())
        elif self.radioButton_2.isChecked():
            gray = filters.Gaussian(gray, (self.horizontalSlider_6.value(), self.horizontalSlider_6.value()), self.horizontalSlider_7.value(), self.horizontalSlider_8.value())
        elif self.radioButton_4.isChecked():
            gray = filters.bilFilter(gray, self.horizontalSlider_9.value(), self.horizontalSlider_10.value(), self.horizontalSlider_11.value())

        #edges = cv2.Canny(gray, self.horizontalSlider.value(), self.horizontalSlider_2.value())
        ret, thresh = cv2.threshold(gray, self.horizontalSlider.value(), self.horizontalSlider_2.value(), 0)

        x1 = self.comboBox.currentIndex()
        x2 = self.comboBox_2.currentIndex()

        c1 = 0
        c2 = 0

        while switch(x1):
            if case(0):
                c1 = cv2.RETR_EXTERNAL
                break
            if case(1):
                c1 = cv2.RETR_LIST
                break
            if case(2):
                c1 = cv2.RETR_CCOMP
                break
            if case(3):
                c1 = cv2.RETR_TREE
                break
            break

        while switch(x2):
            if case(0):
                c2 = cv2.CHAIN_APPROX_NONE
                break
            if case(1):
                c2 = cv2.CHAIN_APPROX_SIMPLE
                break
            if case(2):
                c2 = cv2.CHAIN_APPROX_TC89_L1
                break
            if case(3):
                c2 = cv2.CHAIN_APPROX_TC89_KCOS
                break
            break

        contours, hierarchy = cv2.findContours(thresh,c1,c2)
        if self.checkBox.isChecked():
            for i in range(0, len(contours)):
                contours[i] = cv2.approxPolyDP(contours[i], self.doubleSpinBox.value(), self.checkBox_2.isChecked())
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