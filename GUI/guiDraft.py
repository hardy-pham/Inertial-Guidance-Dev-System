# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUiDraft.ui'
#
# Created: Thu Nov 03 18:00:25 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(MainWindow)
        self.retranslateUi(MainWindow)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(638, 481)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 631, 451))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayoutWidget = QtGui.QWidget(self.tab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(-1, 0, 421, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtGui.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.label_2 = QtGui.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.tab)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 40, 132, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.Gyroscope_On = QtGui.QRadioButton(self.horizontalLayoutWidget_2)
        self.Gyroscope_On.setObjectName("Gyroscope_On")
        self.horizontalLayout_4.addWidget(self.Gyroscope_On)
        self.verticalLayoutWidget = QtGui.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 70, 101, 130))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.GyroRange_125 = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.GyroRange_125.setObjectName("GyroRange_125")
        self.verticalLayout.addWidget(self.GyroRange_125)
        self.GyroRange_245 = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.GyroRange_245.setObjectName("GyroRange_245")
        self.verticalLayout.addWidget(self.GyroRange_245)
        self.GyroRange_500 = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.GyroRange_500.setObjectName("GyroRange_500")
        self.verticalLayout.addWidget(self.GyroRange_500)
        self.GyroRange_1000 = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.GyroRange_1000.setObjectName("GyroRange_1000")
        self.verticalLayout.addWidget(self.GyroRange_1000)
        self.GyroRange_2000 = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.GyroRange_2000.setObjectName("GyroRange_2000")
        self.verticalLayout.addWidget(self.GyroRange_2000)
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.tab)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 200, 101, 199))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.GyroSampleRate_13 = QtGui.QRadioButton(self.verticalLayoutWidget_2)
        self.GyroSampleRate_13.setObjectName("GyroSampleRate_13")
        self.verticalLayout_2.addWidget(self.GyroSampleRate_13)
        self.GyroSampleRate_26 = QtGui.QRadioButton(self.verticalLayoutWidget_2)
        self.GyroSampleRate_26.setObjectName("GyroSampleRate_26")
        self.verticalLayout_2.addWidget(self.GyroSampleRate_26)
        self.GyroSampleRate_52 = QtGui.QRadioButton(self.verticalLayoutWidget_2)
        self.GyroSampleRate_52.setObjectName("GyroSampleRate_52")
        self.verticalLayout_2.addWidget(self.GyroSampleRate_52)
        self.GyroSampleRate_104 = QtGui.QRadioButton(self.verticalLayoutWidget_2)
        self.GyroSampleRate_104.setObjectName("GyroSampleRate_104")
        self.verticalLayout_2.addWidget(self.GyroSampleRate_104)
        self.GyroSampleRate_208 = QtGui.QRadioButton(self.verticalLayoutWidget_2)
        self.GyroSampleRate_208.setObjectName("GyroSampleRate_208")
        self.verticalLayout_2.addWidget(self.GyroSampleRate_208)
        self.GyroSampleRate_416 = QtGui.QRadioButton(self.verticalLayoutWidget_2)
        self.GyroSampleRate_416.setObjectName("GyroSampleRate_416")
        self.verticalLayout_2.addWidget(self.GyroSampleRate_416)
        self.GyroSampleRate_833 = QtGui.QRadioButton(self.verticalLayoutWidget_2)
        self.GyroSampleRate_833.setObjectName("GyroSampleRate_833")
        self.verticalLayout_2.addWidget(self.GyroSampleRate_833)
        self.GyroSampleRate_1666 = QtGui.QRadioButton(self.verticalLayoutWidget_2)
        self.GyroSampleRate_1666.setObjectName("GyroSampleRate_1666")
        self.verticalLayout_2.addWidget(self.GyroSampleRate_1666)
        self.verticalLayoutWidget_5 = QtGui.QWidget(self.tab)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(100, 70, 82, 131))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_11 = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_6.addWidget(self.label_11)
        self.GyroBandwidth_50 = QtGui.QRadioButton(self.verticalLayoutWidget_5)
        self.GyroBandwidth_50.setObjectName("GyroBandwidth_50")
        self.verticalLayout_6.addWidget(self.GyroBandwidth_50)
        self.GyroBandwidth_100 = QtGui.QRadioButton(self.verticalLayoutWidget_5)
        self.GyroBandwidth_100.setObjectName("GyroBandwidth_100")
        self.verticalLayout_6.addWidget(self.GyroBandwidth_100)
        self.GyroBandwidth_200 = QtGui.QRadioButton(self.verticalLayoutWidget_5)
        self.GyroBandwidth_200.setObjectName("GyroBandwidth_200")
        self.verticalLayout_6.addWidget(self.GyroBandwidth_200)
        self.GyroBandwidth_400 = QtGui.QRadioButton(self.verticalLayoutWidget_5)
        self.GyroBandwidth_400.setObjectName("GyroBandwidth_400")
        self.verticalLayout_6.addWidget(self.GyroBandwidth_400)
        self.verticalLayoutWidget_6 = QtGui.QWidget(self.tab)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(100, 200, 61, 81))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_12 = QtGui.QLabel(self.verticalLayoutWidget_6)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_7.addWidget(self.label_12)
        self.GyroFIFO_ON = QtGui.QRadioButton(self.verticalLayoutWidget_6)
        self.GyroFIFO_ON.setObjectName("GyroFIFO_ON")
        self.verticalLayout_7.addWidget(self.GyroFIFO_ON)
        self.GyroFIFO_OFF = QtGui.QRadioButton(self.verticalLayoutWidget_6)
        self.GyroFIFO_OFF.setObjectName("GyroFIFO_OFF")
        self.verticalLayout_7.addWidget(self.GyroFIFO_OFF)
        self.verticalLayoutWidget_7 = QtGui.QWidget(self.tab)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(100, 280, 104, 81))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_13 = QtGui.QLabel(self.verticalLayoutWidget_7)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_8.addWidget(self.label_13)
        self.GyroFIFODec_ON = QtGui.QRadioButton(self.verticalLayoutWidget_7)
        self.GyroFIFODec_ON.setObjectName("GyroFIFODec_ON")
        self.verticalLayout_8.addWidget(self.GyroFIFODec_ON)
        self.GyroFIFODEC_OFF = QtGui.QRadioButton(self.verticalLayoutWidget_7)
        self.GyroFIFODEC_OFF.setObjectName("GyroFIFODEC_OFF")
        self.verticalLayout_8.addWidget(self.GyroFIFODEC_OFF)
        self.horizontalLayoutWidget_5 = QtGui.QWidget(self.tab)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(220, 40, 207, 31))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_14 = QtGui.QLabel(self.horizontalLayoutWidget_5)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_7.addWidget(self.label_14)
        self.Accelerometer_ON = QtGui.QRadioButton(self.horizontalLayoutWidget_5)
        self.Accelerometer_ON.setObjectName("Accelerometer_ON")
        self.horizontalLayout_7.addWidget(self.Accelerometer_ON)
        self.verticalLayoutWidget_8 = QtGui.QWidget(self.tab)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(220, 70, 101, 111))
        self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_15 = QtGui.QLabel(self.verticalLayoutWidget_8)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_9.addWidget(self.label_15)
        self.AccelRange_2 = QtGui.QRadioButton(self.verticalLayoutWidget_8)
        self.AccelRange_2.setObjectName("AccelRange_2")
        self.verticalLayout_9.addWidget(self.AccelRange_2)
        self.AccelRange_4 = QtGui.QRadioButton(self.verticalLayoutWidget_8)
        self.AccelRange_4.setObjectName("AccelRange_4")
        self.verticalLayout_9.addWidget(self.AccelRange_4)
        self.AccelRange_8 = QtGui.QRadioButton(self.verticalLayoutWidget_8)
        self.AccelRange_8.setObjectName("AccelRange_8")
        self.verticalLayout_9.addWidget(self.AccelRange_8)
        self.AccelRange_16 = QtGui.QRadioButton(self.verticalLayoutWidget_8)
        self.AccelRange_16.setObjectName("AccelRange_16")
        self.verticalLayout_9.addWidget(self.AccelRange_16)
        self.verticalLayoutWidget_9 = QtGui.QWidget(self.tab)
        self.verticalLayoutWidget_9.setGeometry(QtCore.QRect(320, 70, 86, 131))
        self.verticalLayoutWidget_9.setObjectName("verticalLayoutWidget_9")
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_16 = QtGui.QLabel(self.verticalLayoutWidget_9)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_10.addWidget(self.label_16)
        self.AccelBandWidth_50 = QtGui.QRadioButton(self.verticalLayoutWidget_9)
        self.AccelBandWidth_50.setObjectName("AccelBandWidth_50")
        self.verticalLayout_10.addWidget(self.AccelBandWidth_50)
        self.AccelBandWidth_100 = QtGui.QRadioButton(self.verticalLayoutWidget_9)
        self.AccelBandWidth_100.setObjectName("AccelBandWidth_100")
        self.verticalLayout_10.addWidget(self.AccelBandWidth_100)
        self.AccelBandWidth_200 = QtGui.QRadioButton(self.verticalLayoutWidget_9)
        self.AccelBandWidth_200.setObjectName("AccelBandWidth_200")
        self.verticalLayout_10.addWidget(self.AccelBandWidth_200)
        self.AccelBandWidth_400 = QtGui.QRadioButton(self.verticalLayoutWidget_9)
        self.AccelBandWidth_400.setObjectName("AccelBandWidth_400")
        self.verticalLayout_10.addWidget(self.AccelBandWidth_400)
        self.verticalLayoutWidget_10 = QtGui.QWidget(self.tab)
        self.verticalLayoutWidget_10.setGeometry(QtCore.QRect(220, 178, 101, 231))
        self.verticalLayoutWidget_10.setObjectName("verticalLayoutWidget_10")
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.verticalLayoutWidget_10)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_17 = QtGui.QLabel(self.verticalLayoutWidget_10)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_11.addWidget(self.label_17)
        self.AccelSampleRate_13 = QtGui.QRadioButton(self.verticalLayoutWidget_10)
        self.AccelSampleRate_13.setObjectName("AccelSampleRate_13")
        self.verticalLayout_11.addWidget(self.AccelSampleRate_13)
        self.AccelSampleRate_26 = QtGui.QRadioButton(self.verticalLayoutWidget_10)
        self.AccelSampleRate_26.setObjectName("AccelSampleRate_26")
        self.verticalLayout_11.addWidget(self.AccelSampleRate_26)
        self.AccelSampleRate_52 = QtGui.QRadioButton(self.verticalLayoutWidget_10)
        self.AccelSampleRate_52.setObjectName("AccelSampleRate_52")
        self.verticalLayout_11.addWidget(self.AccelSampleRate_52)
        self.AccelSampleRate_104 = QtGui.QRadioButton(self.verticalLayoutWidget_10)
        self.AccelSampleRate_104.setObjectName("AccelSampleRate_104")
        self.verticalLayout_11.addWidget(self.AccelSampleRate_104)
        self.AccelSampleRate_208 = QtGui.QRadioButton(self.verticalLayoutWidget_10)
        self.AccelSampleRate_208.setObjectName("AccelSampleRate_208")
        self.verticalLayout_11.addWidget(self.AccelSampleRate_208)
        self.AccelSampleRate_416 = QtGui.QRadioButton(self.verticalLayoutWidget_10)
        self.AccelSampleRate_416.setObjectName("AccelSampleRate_416")
        self.verticalLayout_11.addWidget(self.AccelSampleRate_416)
        self.AccelSampleRate_833 = QtGui.QRadioButton(self.verticalLayoutWidget_10)
        self.AccelSampleRate_833.setObjectName("AccelSampleRate_833")
        self.verticalLayout_11.addWidget(self.AccelSampleRate_833)
        self.AccelSampleRate_1666 = QtGui.QRadioButton(self.verticalLayoutWidget_10)
        self.AccelSampleRate_1666.setObjectName("AccelSampleRate_1666")
        self.verticalLayout_11.addWidget(self.AccelSampleRate_1666)
        self.AccelSampleRate_3332 = QtGui.QRadioButton(self.verticalLayoutWidget_10)
        self.AccelSampleRate_3332.setObjectName("AccelSampleRate_3332")
        self.verticalLayout_11.addWidget(self.AccelSampleRate_3332)
        self.AccelSampleRate_6664 = QtGui.QRadioButton(self.verticalLayoutWidget_10)
        self.AccelSampleRate_6664.setObjectName("AccelSampleRate_6664")
        self.verticalLayout_11.addWidget(self.AccelSampleRate_6664)
        self.AccelSampleRate_13330 = QtGui.QRadioButton(self.verticalLayoutWidget_10)
        self.AccelSampleRate_13330.setObjectName("AccelSampleRate_13330")
        self.verticalLayout_11.addWidget(self.AccelSampleRate_13330)
        self.verticalLayoutWidget_11 = QtGui.QWidget(self.tab)
        self.verticalLayoutWidget_11.setGeometry(QtCore.QRect(320, 200, 61, 81))
        self.verticalLayoutWidget_11.setObjectName("verticalLayoutWidget_11")
        self.verticalLayout_12 = QtGui.QVBoxLayout(self.verticalLayoutWidget_11)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_18 = QtGui.QLabel(self.verticalLayoutWidget_11)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_12.addWidget(self.label_18)
        self.AccelFIFO_ON = QtGui.QRadioButton(self.verticalLayoutWidget_11)
        self.AccelFIFO_ON.setObjectName("AccelFIFO_ON")
        self.verticalLayout_12.addWidget(self.AccelFIFO_ON)
        self.AccelFIFO_OFF = QtGui.QRadioButton(self.verticalLayoutWidget_11)
        self.AccelFIFO_OFF.setObjectName("AccelFIFO_OFF")
        self.verticalLayout_12.addWidget(self.AccelFIFO_OFF)
        self.verticalLayoutWidget_12 = QtGui.QWidget(self.tab)
        self.verticalLayoutWidget_12.setGeometry(QtCore.QRect(320, 280, 106, 81))
        self.verticalLayoutWidget_12.setObjectName("verticalLayoutWidget_12")
        self.verticalLayout_13 = QtGui.QVBoxLayout(self.verticalLayoutWidget_12)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_19 = QtGui.QLabel(self.verticalLayoutWidget_12)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_13.addWidget(self.label_19)
        self.AccelFIFODEC_ON = QtGui.QRadioButton(self.verticalLayoutWidget_12)
        self.AccelFIFODEC_ON.setObjectName("AccelFIFODEC_ON")
        self.verticalLayout_13.addWidget(self.AccelFIFODEC_ON)
        self.AccelFIFODEC_OFF = QtGui.QRadioButton(self.verticalLayoutWidget_12)
        self.AccelFIFODEC_OFF.setObjectName("AccelFIFODEC_OFF")
        self.verticalLayout_13.addWidget(self.AccelFIFODEC_OFF)
        self.label_20 = QtGui.QLabel(self.tab)
        self.label_20.setGeometry(QtCore.QRect(470, 0, 236, 39))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.FIFO_Threshold = QtGui.QDoubleSpinBox(self.tab)
        self.FIFO_Threshold.setGeometry(QtCore.QRect(520, 50, 101, 21))
        self.FIFO_Threshold.setObjectName("FIFO_Threshold")
        self.label_21 = QtGui.QLabel(self.tab)
        self.label_21.setGeometry(QtCore.QRect(450, 50, 71, 21))
        self.label_21.setObjectName("label_21")
        self.FIFO_SampleRate = QtGui.QDoubleSpinBox(self.tab)
        self.FIFO_SampleRate.setGeometry(QtCore.QRect(520, 90, 101, 21))
        self.FIFO_SampleRate.setObjectName("FIFO_SampleRate")
        self.label_22 = QtGui.QLabel(self.tab)
        self.label_22.setGeometry(QtCore.QRect(440, 90, 71, 21))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtGui.QLabel(self.tab)
        self.label_23.setGeometry(QtCore.QRect(440, 120, 61, 20))
        self.label_23.setObjectName("label_23")
        self.ModeWord_ON = QtGui.QRadioButton(self.tab)
        self.ModeWord_ON.setGeometry(QtCore.QRect(520, 140, 104, 17))
        self.ModeWord_ON.setObjectName("ModeWord_ON")
        self.ModeWord_OFF = QtGui.QRadioButton(self.tab)
        self.ModeWord_OFF.setGeometry(QtCore.QRect(520, 170, 104, 17))
        self.ModeWord_OFF.setObjectName("ModeWord_OFF")
        self.label_24 = QtGui.QLabel(self.tab)
        self.label_24.setGeometry(QtCore.QRect(450, 210, 236, 39))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.CommMode_1 = QtGui.QRadioButton(self.tab)
        self.CommMode_1.setGeometry(QtCore.QRect(501, 240, 111, 20))
        self.CommMode_1.setObjectName("CommMode_1")
        self.CommMode_2 = QtGui.QRadioButton(self.tab)
        self.CommMode_2.setGeometry(QtCore.QRect(501, 260, 111, 20))
        self.CommMode_2.setObjectName("CommMode_2")
        self.CommMode_3 = QtGui.QRadioButton(self.tab)
        self.CommMode_3.setGeometry(QtCore.QRect(501, 280, 111, 20))
        self.CommMode_3.setObjectName("CommMode_3")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 638, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "LSM6DS3 Interface", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Gyroscope Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Accelerometer Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", " Enable", None, QtGui.QApplication.UnicodeUTF8))
        self.Gyroscope_On.setText(QtGui.QApplication.translate("MainWindow", "Gyroscope on", None, QtGui.QApplication.UnicodeUTF8))

        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "GyroRange:", None, QtGui.QApplication.UnicodeUTF8))
        self.GyroRange_125.setText(QtGui.QApplication.translate("MainWindow", "125 deg/s", None, QtGui.QApplication.UnicodeUTF8))

        self.GyroRange_245.setText(QtGui.QApplication.translate("MainWindow", "245 deg/s", None, QtGui.QApplication.UnicodeUTF8))

        self.GyroRange_500.setText(QtGui.QApplication.translate("MainWindow", "500 deg/s", None, QtGui.QApplication.UnicodeUTF8))

        self.GyroRange_1000.setText(QtGui.QApplication.translate("MainWindow", "1000 deg/s", None, QtGui.QApplication.UnicodeUTF8))

        self.GyroRange_2000.setText(QtGui.QApplication.translate("MainWindow", "2000 deg/s", None, QtGui.QApplication.UnicodeUTF8))
     
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Gyro Sample Rate:", None, QtGui.QApplication.UnicodeUTF8))
        self.GyroSampleRate_13.setText(QtGui.QApplication.translate("MainWindow", "13 Hz", None, QtGui.QApplication.UnicodeUTF8))
        self.GyroSampleRate_26.setText(QtGui.QApplication.translate("MainWindow", "26 Hz", None, QtGui.QApplication.UnicodeUTF8))
        self.GyroSampleRate_52.setText(QtGui.QApplication.translate("MainWindow", "52 Hz", None, QtGui.QApplication.UnicodeUTF8))
        self.GyroSampleRate_104.setText(QtGui.QApplication.translate("MainWindow", "104 Hz", None, QtGui.QApplication.UnicodeUTF8))
        self.GyroSampleRate_208.setText(QtGui.QApplication.translate("MainWindow", "208 Hz", None, QtGui.QApplication.UnicodeUTF8))
        self.GyroSampleRate_416.setText(QtGui.QApplication.translate("MainWindow", "416 Hz", None, QtGui.QApplication.UnicodeUTF8))
        self.GyroSampleRate_833.setText(QtGui.QApplication.translate("MainWindow", "833 Hz", None, QtGui.QApplication.UnicodeUTF8))
        self.GyroSampleRate_1666.setText(QtGui.QApplication.translate("MainWindow", "1666 Hz", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("MainWindow", "Gyro Bandwidth:", None, QtGui.QApplication.UnicodeUTF8))
        self.GyroBandwidth_50.setText(QtGui.QApplication.translate("MainWindow", "50 Hz", None, QtGui.QApplication.UnicodeUTF8))
        self.GyroBandwidth_100.setText(QtGui.QApplication.translate("MainWindow", "100 Hz", None, QtGui.QApplication.UnicodeUTF8))
        self.GyroBandwidth_200.setText(QtGui.QApplication.translate("MainWindow", "200 Hz", None, QtGui.QApplication.UnicodeUTF8))
        self.GyroBandwidth_400.setText(QtGui.QApplication.translate("MainWindow", "400 Hz", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("MainWindow", "GyroFIFO:", None, QtGui.QApplication.UnicodeUTF8))
        self.GyroFIFO_ON.setText(QtGui.QApplication.translate("MainWindow", "On", None, QtGui.QApplication.UnicodeUTF8))
        self.GyroFIFO_OFF.setText(QtGui.QApplication.translate("MainWindow", "Off", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("MainWindow", "GyroFIFO Decimation", None, QtGui.QApplication.UnicodeUTF8))
        self.GyroFIFODec_ON.setText(QtGui.QApplication.translate("MainWindow", "On", None, QtGui.QApplication.UnicodeUTF8))
        self.GyroFIFODEC_OFF.setText(QtGui.QApplication.translate("MainWindow", "Off", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("MainWindow", " Enable", None, QtGui.QApplication.UnicodeUTF8))
        self.Accelerometer_ON.setText(QtGui.QApplication.translate("MainWindow", "Accelorometer", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("MainWindow", "AccelRange:", None, QtGui.QApplication.UnicodeUTF8))
        self.AccelRange_2.setText(QtGui.QApplication.translate("MainWindow", "2 G", None, QtGui.QApplication.UnicodeUTF8))
        self.AccelRange_4.setText(QtGui.QApplication.translate("MainWindow", "4 G", None, QtGui.QApplication.UnicodeUTF8))
        self.AccelRange_8.setText(QtGui.QApplication.translate("MainWindow", "8 G", None, QtGui.QApplication.UnicodeUTF8))
        self.AccelRange_16.setText(QtGui.QApplication.translate("MainWindow", "16 G", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("MainWindow", "Accel Bandwidth:", None, QtGui.QApplication.UnicodeUTF8))
        self.AccelBandWidth_50.setText(QtGui.QApplication.translate("MainWindow", "50 Hz", None, QtGui.QApplication.UnicodeUTF8))
        self.AccelBandWidth_100.setText(QtGui.QApplication.translate("MainWindow", "100 Hz", None, QtGui.QApplication.UnicodeUTF8))
        self.AccelBandWidth_200.setText(QtGui.QApplication.translate("MainWindow", "200 Hz", None, QtGui.QApplication.UnicodeUTF8))
        self.AccelBandWidth_400.setText(QtGui.QApplication.translate("MainWindow", "400 Hz", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("MainWindow", "Accel Sample Rate:", None, QtGui.QApplication.UnicodeUTF8))
        self.AccelSampleRate_13.setText(QtGui.QApplication.translate("MainWindow", "13 Hz", None, QtGui.QApplication.UnicodeUTF8))
        self.AccelSampleRate_26.setText(QtGui.QApplication.translate("MainWindow", "26 Hz", None, QtGui.QApplication.UnicodeUTF8))
        self.AccelSampleRate_52.setText(QtGui.QApplication.translate("MainWindow", "52 Hz", None, QtGui.QApplication.UnicodeUTF8))
        self.AccelSampleRate_104.setText(QtGui.QApplication.translate("MainWindow", "104 Hz", None, QtGui.QApplication.UnicodeUTF8))
        self.AccelSampleRate_208.setText(QtGui.QApplication.translate("MainWindow", "208 Hz", None, QtGui.QApplication.UnicodeUTF8))
        self.AccelSampleRate_416.setText(QtGui.QApplication.translate("MainWindow", "416 Hz", None, QtGui.QApplication.UnicodeUTF8))
        self.AccelSampleRate_833.setText(QtGui.QApplication.translate("MainWindow", "833 Hz", None, QtGui.QApplication.UnicodeUTF8))
        self.AccelSampleRate_1666.setText(QtGui.QApplication.translate("MainWindow", "1666 Hz", None, QtGui.QApplication.UnicodeUTF8))
        self.AccelSampleRate_3332.setText(QtGui.QApplication.translate("MainWindow", "3332 Hz", None, QtGui.QApplication.UnicodeUTF8))
        self.AccelSampleRate_6664.setText(QtGui.QApplication.translate("MainWindow", "6664 Hz", None, QtGui.QApplication.UnicodeUTF8))
        self.AccelSampleRate_13330.setText(QtGui.QApplication.translate("MainWindow", "13330 Hz", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("MainWindow", "AccelFIFO:", None, QtGui.QApplication.UnicodeUTF8))
        self.AccelFIFO_ON.setText(QtGui.QApplication.translate("MainWindow", "On", None, QtGui.QApplication.UnicodeUTF8))
        self.AccelFIFO_OFF.setText(QtGui.QApplication.translate("MainWindow", "Off", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("MainWindow", "AccelFIFO Decimation", None, QtGui.QApplication.UnicodeUTF8))
        self.AccelFIFODEC_ON.setText(QtGui.QApplication.translate("MainWindow", "On", None, QtGui.QApplication.UnicodeUTF8))
        self.AccelFIFODEC_OFF.setText(QtGui.QApplication.translate("MainWindow", "Off", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate("MainWindow", "FIFO Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setText(QtGui.QApplication.translate("MainWindow", "ThresHold", None, QtGui.QApplication.UnicodeUTF8))
        self.label_22.setText(QtGui.QApplication.translate("MainWindow", "Sample Rate", None, QtGui.QApplication.UnicodeUTF8))
        self.label_23.setText(QtGui.QApplication.translate("MainWindow", "Mode Word:", None, QtGui.QApplication.UnicodeUTF8))
        self.ModeWord_ON.setText(QtGui.QApplication.translate("MainWindow", "On", None, QtGui.QApplication.UnicodeUTF8))
        self.ModeWord_OFF.setText(QtGui.QApplication.translate("MainWindow", "Off", None, QtGui.QApplication.UnicodeUTF8))
        self.label_24.setText(QtGui.QApplication.translate("MainWindow", "Comm Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.CommMode_1.setText(QtGui.QApplication.translate("MainWindow", "Accelerometer only", None, QtGui.QApplication.UnicodeUTF8))
        self.CommMode_2.setText(QtGui.QApplication.translate("MainWindow", "Gyroscope only", None, QtGui.QApplication.UnicodeUTF8))
        self.CommMode_3.setText(QtGui.QApplication.translate("MainWindow", "Both", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "Registers", None, QtGui.QApplication.UnicodeUTF8))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())