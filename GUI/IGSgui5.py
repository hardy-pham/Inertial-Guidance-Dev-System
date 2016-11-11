# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IGSgui.ui'
#
# Created: Wed Nov  9 02:52:40 2016
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
# from LSM6DS3 import *
# from LSM6DS3_Registers import *

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
        def runAccelerometer(self):
            test=LSM6DS3()
            test.begin()
            test.printAccelXYZ()
        def runGyroscope(self):
            test=LSM6DS3()
            test.begin()
            test.printGyroXYZ()
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(621, 637)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, 30, 121, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(390, 500, 171, 31))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(390, 460, 171, 31))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(70, 60, 191, 31))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 30, 171, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 110, 191, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 190, 191, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(240, 260, 71, 31))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 330, 201, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.checkBox = QtGui.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(100, 360, 141, 26))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.checkBox_2 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(250, 360, 121, 26))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.checkBox_3 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(380, 360, 131, 26))
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 460, 151, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(230, 470, 141, 51))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(350, 60, 221, 261))
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(70, 220, 151, 33))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(70, 150, 121, 21))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(50, 420, 21, 21))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(160, 420, 16, 21))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(270, 420, 16, 21))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(70, 420, 71, 21))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(180, 420, 71, 21))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(290, 420, 71, 21))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.pushButton_6 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(50, 500, 151, 31))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.label_14 = QtGui.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(350, 90, 261, 21))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 621, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))


        self.pushButton.clicked.connect(runAccelerometer)
        self.pushButton_6.clicked.connect(runGyroscope)

        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        self.comboBox.setCurrentIndex(0)
        QtCore.QObject.connect(self.comboBox, QtCore.SIGNAL(_fromUtf8("activated(int)")), self.label_7.setNum)
        QtCore.QObject.connect(self.comboBox, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(QString)")), self.label_6.setText)
        QtCore.QObject.connect(self.lineEdit, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.label_7.setText)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Description:", None))
        self.pushButton_2.setText(_translate("MainWindow", "Pause Graph", None))
        self.pushButton_3.setText(_translate("MainWindow", "Display Graph", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "Bandwidth", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "Sample Rate", None))
        self.comboBox.setItemText(2, _translate("MainWindow", "Accelerometer Range", None))
        self.comboBox.setItemText(3, _translate("MainWindow", "Gyroscope Range", None))
        self.label_2.setText(_translate("MainWindow", "Setting:", None))
        self.label_3.setText(_translate("MainWindow", "Current Register Value:", None))
        self.label_4.setText(_translate("MainWindow", "Change Register Value to:", None))
        self.pushButton_4.setText(_translate("MainWindow", "Change", None))
        self.label_5.setText(_translate("MainWindow", "Operation Mode:", None))
        self.checkBox.setText(_translate("MainWindow", "Accelerometer", None))
        self.checkBox_2.setText(_translate("MainWindow", "Gyroscope", None))
        self.checkBox_3.setText(_translate("MainWindow", "Temperature", None))
        self.pushButton.setText(_translate("MainWindow", "Run Accelerometer", None))
        self.pushButton_5.setText(_translate("MainWindow", "Stop", None))
        self.label_6.setText(_translate("MainWindow", "Description of register", None))
        self.label_7.setText(_translate("MainWindow", "Value", None))
        self.label_8.setText(_translate("MainWindow", "X:", None))
        self.label_9.setText(_translate("MainWindow", "Y:", None))
        self.label_10.setText(_translate("MainWindow", "Z:", None))
        self.label_11.setText(_translate("MainWindow", "null", None))
        self.label_12.setText(_translate("MainWindow", "null", None))
        self.label_13.setText(_translate("MainWindow", "null", None))
        self.pushButton_6.setText(_translate("MainWindow", "Run Gyroscope", None))
        self.label_14.setText(_translate("MainWindow", "Possible values for the setting", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

