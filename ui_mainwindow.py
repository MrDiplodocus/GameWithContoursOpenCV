# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Mon Feb 23 23:18:25 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(829, 719)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 10, 531, 571))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(550, 10, 271, 681))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.widget = QtGui.QWidget(self.tab)
        self.widget.setGeometry(QtCore.QRect(10, 10, 251, 641))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.pShowOriginal = QtGui.QPushButton(self.widget)
        self.pShowOriginal.setObjectName(_fromUtf8("pShowOriginal"))
        self.verticalLayout_2.addWidget(self.pShowOriginal)
        self.groupBox_2 = QtGui.QGroupBox(self.widget)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.rAuto = QtGui.QRadioButton(self.groupBox_2)
        self.rAuto.setChecked(True)
        self.rAuto.setObjectName(_fromUtf8("rAuto"))
        self.verticalLayout.addWidget(self.rAuto)
        self.rManual = QtGui.QRadioButton(self.groupBox_2)
        self.rManual.setEnabled(False)
        self.rManual.setObjectName(_fromUtf8("rManual"))
        self.verticalLayout.addWidget(self.rManual)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(self.widget)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label = QtGui.QLabel(self.groupBox_3)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_5.addWidget(self.label)
        self.label_2 = QtGui.QLabel(self.groupBox_3)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_5.addWidget(self.label_2)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalSlider = QtGui.QSlider(self.groupBox_3)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.verticalLayout_3.addWidget(self.horizontalSlider)
        self.horizontalSlider_2 = QtGui.QSlider(self.groupBox_3)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName(_fromUtf8("horizontalSlider_2"))
        self.verticalLayout_3.addWidget(self.horizontalSlider_2)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_9.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.groupBox_4 = QtGui.QGroupBox(self.widget)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.chCanny = QtGui.QCheckBox(self.groupBox_4)
        self.chCanny.setObjectName(_fromUtf8("chCanny"))
        self.verticalLayout_4.addWidget(self.chCanny)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.label_5 = QtGui.QLabel(self.groupBox_4)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_6.addWidget(self.label_5)
        self.horizontalSlider_3 = QtGui.QSlider(self.groupBox_4)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName(_fromUtf8("horizontalSlider_3"))
        self.verticalLayout_6.addWidget(self.horizontalSlider_3)
        self.verticalLayout_4.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.label_6 = QtGui.QLabel(self.groupBox_4)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_7.addWidget(self.label_6)
        self.horizontalSlider_4 = QtGui.QSlider(self.groupBox_4)
        self.horizontalSlider_4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_4.setObjectName(_fromUtf8("horizontalSlider_4"))
        self.verticalLayout_7.addWidget(self.horizontalSlider_4)
        self.verticalLayout_4.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.label_7 = QtGui.QLabel(self.groupBox_4)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_8.addWidget(self.label_7)
        self.horizontalSlider_5 = QtGui.QSlider(self.groupBox_4)
        self.horizontalSlider_5.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_5.setObjectName(_fromUtf8("horizontalSlider_5"))
        self.verticalLayout_8.addWidget(self.horizontalSlider_5)
        self.verticalLayout_4.addLayout(self.verticalLayout_8)
        self.chL2Gradient = QtGui.QCheckBox(self.groupBox_4)
        self.chL2Gradient.setObjectName(_fromUtf8("chL2Gradient"))
        self.verticalLayout_4.addWidget(self.chL2Gradient)
        self.verticalLayout_2.addWidget(self.groupBox_4)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_4)
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.label_3)
        self.comboBox = QtGui.QComboBox(self.widget)
        self.comboBox.setEditable(False)
        self.comboBox.setDuplicatesEnabled(False)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.comboBox)
        self.comboBox_2 = QtGui.QComboBox(self.widget)
        self.comboBox_2.setEditable(False)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.comboBox_2)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.groupBox_5 = QtGui.QGroupBox(self.widget)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.checkBox = QtGui.QCheckBox(self.groupBox_5)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.verticalLayout_10.addWidget(self.checkBox)
        self.doubleSpinBox = QtGui.QDoubleSpinBox(self.groupBox_5)
        self.doubleSpinBox.setProperty("value", 0.5)
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.verticalLayout_10.addWidget(self.doubleSpinBox)
        self.verticalLayout_2.addWidget(self.groupBox_5)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 580, 531, 111))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.widget1 = QtGui.QWidget(self.groupBox)
        self.widget1.setGeometry(QtCore.QRect(10, 20, 511, 90))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.widget1)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.verticalLayout_11 = QtGui.QVBoxLayout()
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.radioButton = QtGui.QRadioButton(self.widget1)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.verticalLayout_11.addWidget(self.radioButton)
        self.radioButton_2 = QtGui.QRadioButton(self.widget1)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.verticalLayout_11.addWidget(self.radioButton_2)
        self.radioButton_3 = QtGui.QRadioButton(self.widget1)
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.verticalLayout_11.addWidget(self.radioButton_3)
        self.radioButton_4 = QtGui.QRadioButton(self.widget1)
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))
        self.verticalLayout_11.addWidget(self.radioButton_4)
        self.horizontalLayout_5.addLayout(self.verticalLayout_11)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout_15 = QtGui.QVBoxLayout()
        self.verticalLayout_15.setObjectName(_fromUtf8("verticalLayout_15"))
        self.label_8 = QtGui.QLabel(self.widget1)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_15.addWidget(self.label_8)
        self.label_9 = QtGui.QLabel(self.widget1)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout_15.addWidget(self.label_9)
        self.label_10 = QtGui.QLabel(self.widget1)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.verticalLayout_15.addWidget(self.label_10)
        self.horizontalLayout_3.addLayout(self.verticalLayout_15)
        self.verticalLayout_14 = QtGui.QVBoxLayout()
        self.verticalLayout_14.setObjectName(_fromUtf8("verticalLayout_14"))
        self.horizontalSlider_6 = QtGui.QSlider(self.widget1)
        self.horizontalSlider_6.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_6.setObjectName(_fromUtf8("horizontalSlider_6"))
        self.verticalLayout_14.addWidget(self.horizontalSlider_6)
        self.horizontalSlider_7 = QtGui.QSlider(self.widget1)
        self.horizontalSlider_7.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_7.setObjectName(_fromUtf8("horizontalSlider_7"))
        self.verticalLayout_14.addWidget(self.horizontalSlider_7)
        self.horizontalSlider_8 = QtGui.QSlider(self.widget1)
        self.horizontalSlider_8.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_8.setObjectName(_fromUtf8("horizontalSlider_8"))
        self.verticalLayout_14.addWidget(self.horizontalSlider_8)
        self.horizontalLayout_3.addLayout(self.verticalLayout_14)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_13 = QtGui.QVBoxLayout()
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        self.label_11 = QtGui.QLabel(self.widget1)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.verticalLayout_13.addWidget(self.label_11)
        self.label_12 = QtGui.QLabel(self.widget1)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.verticalLayout_13.addWidget(self.label_12)
        self.label_13 = QtGui.QLabel(self.widget1)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.verticalLayout_13.addWidget(self.label_13)
        self.horizontalLayout_2.addLayout(self.verticalLayout_13)
        self.verticalLayout_12 = QtGui.QVBoxLayout()
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.horizontalSlider_9 = QtGui.QSlider(self.widget1)
        self.horizontalSlider_9.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_9.setObjectName(_fromUtf8("horizontalSlider_9"))
        self.verticalLayout_12.addWidget(self.horizontalSlider_9)
        self.horizontalSlider_10 = QtGui.QSlider(self.widget1)
        self.horizontalSlider_10.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_10.setObjectName(_fromUtf8("horizontalSlider_10"))
        self.verticalLayout_12.addWidget(self.horizontalSlider_10)
        self.horizontalSlider_11 = QtGui.QSlider(self.widget1)
        self.horizontalSlider_11.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_11.setObjectName(_fromUtf8("horizontalSlider_11"))
        self.verticalLayout_12.addWidget(self.horizontalSlider_11)
        self.horizontalLayout_2.addLayout(self.verticalLayout_12)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 829, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menuBar)
        self.action = QtGui.QAction(MainWindow)
        self.action.setObjectName(_fromUtf8("action"))
        self.action_2 = QtGui.QAction(MainWindow)
        self.action_2.setObjectName(_fromUtf8("action_2"))
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Поиск контуров", None))
        self.pShowOriginal.setText(_translate("MainWindow", "Показать оригинал", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Режим", None))
        self.rAuto.setText(_translate("MainWindow", "Автоматический", None))
        self.rManual.setText(_translate("MainWindow", "Выделение областей", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "InRange", None))
        self.label.setText(_translate("MainWindow", "Нижний", None))
        self.label_2.setText(_translate("MainWindow", "Верхний", None))
        self.groupBox_4.setTitle(_translate("MainWindow", "Алгоритм Canny", None))
        self.chCanny.setText(_translate("MainWindow", "Вкл./выкл.", None))
        self.label_5.setText(_translate("MainWindow", "Нижний порог", None))
        self.label_6.setText(_translate("MainWindow", "Верхний порог", None))
        self.label_7.setText(_translate("MainWindow", "Размер апертуры для оператора Собеля", None))
        self.chL2Gradient.setText(_translate("MainWindow", "L2gradient", None))
        self.label_4.setText(_translate("MainWindow", "Mode", None))
        self.label_3.setText(_translate("MainWindow", "Method", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "Внешние контуры", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "Все контуры", None))
        self.comboBox.setItemText(2, _translate("MainWindow", "CCOMP", None))
        self.comboBox.setItemText(3, _translate("MainWindow", "TREE ", None))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "NONE", None))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "SIMPLE", None))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "L1", None))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "KCOS", None))
        self.groupBox_5.setTitle(_translate("MainWindow", "Аппроксимация", None))
        self.checkBox.setText(_translate("MainWindow", "Вкл./выкл.", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Основное", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Инструменты", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Информация", None))
        self.groupBox.setTitle(_translate("MainWindow", "Фильтр", None))
        self.radioButton.setText(_translate("MainWindow", "Кувахара", None))
        self.radioButton_2.setText(_translate("MainWindow", "Гаусс", None))
        self.radioButton_3.setText(_translate("MainWindow", "Медиана", None))
        self.radioButton_4.setText(_translate("MainWindow", "Двусторонний", None))
        self.label_8.setText(_translate("MainWindow", "Kernel_Size", None))
        self.label_9.setText(_translate("MainWindow", "SigmaX", None))
        self.label_10.setText(_translate("MainWindow", "SigmaY", None))
        self.label_11.setText(_translate("MainWindow", "Diameter", None))
        self.label_12.setText(_translate("MainWindow", "SigmaColor", None))
        self.label_13.setText(_translate("MainWindow", "SigmaSpace", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.action.setText(_translate("MainWindow", "Open", None))
        self.action_2.setText(_translate("MainWindow", "Save contours", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))

