# -*- coding: utf-8 -*-
#!/usr/bin/env python3

# Filename: PLC.py

"""PLC is a simple password leak finder that checks if your password has ever been leaked."""

__version__ = '0.1'
__author__ = 'Adrian Gąsior'


import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from plf_requests import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(865, 325)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.run = QtWidgets.QPushButton(self.centralwidget)
        self.run.setGeometry(QtCore.QRect(750, 110, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setWeight(50)
        self.run.setFont(font)
        self.run.setObjectName("run")
        # mine code
        self.run.clicked.connect(self.run_and_store)
        self.quit = QtWidgets.QPushButton(self.centralwidget)
        self.quit.setGeometry(QtCore.QRect(750, 200, 71, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.quit.setFont(font)
        self.quit.setObjectName("quit")
        self.quit.clicked.connect(self.exit_app)
        self.how_to = QtWidgets.QLabel(self.centralwidget)
        self.how_to.setGeometry(QtCore.QRect(20, 30, 70, 16))
        self.how_to.setObjectName("how_to")
        self.nr_1 = QtWidgets.QLabel(self.centralwidget)
        self.nr_1.setGeometry(QtCore.QRect(20, 50, 321, 16))
        self.nr_1.setObjectName("nr_1")
        self.nr_2 = QtWidgets.QLabel(self.centralwidget)
        self.nr_2.setGeometry(QtCore.QRect(20, 70, 82, 16))
        self.nr_2.setObjectName("nr_2")
        self.nr_3 = QtWidgets.QLabel(self.centralwidget)
        self.nr_3.setGeometry(QtCore.QRect(20, 90, 234, 16))
        self.nr_3.setObjectName("nr_3")
        self.password_input = QtWidgets.QLineEdit(self.centralwidget)
        self.password_input.setGeometry(QtCore.QRect(10, 110, 741, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.password_input.setFont(font)
        self.password_input.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.password_input.setText("")
        self.password_input.setFrame(True)
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.password_input.setCursorPosition(0)
        self.password_input.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.password_input.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.password_input.setObjectName("password_input")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(110, 180, 58, 16))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.result = QtWidgets.QLabel(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(10, 160, 691, 51))
        self.result.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.result.setObjectName("result")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 865, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuAction = QtWidgets.QMenu(self.menuBar)
        self.menuAction.setObjectName("menuAction")
        self.actionAbout_2 = QtWidgets.QAction(MainWindow)
        self.actionAbout_2.setObjectName("actionAbout_2")
        self.actionHow_to_2 = QtWidgets.QAction(MainWindow)
        self.actionHow_to_2.setObjectName("actionHow_to_2")
        self.actionRun = QtWidgets.QAction(MainWindow)
        self.actionRun.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.actionRun.setObjectName("actionRun")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuHelp.addAction(self.actionAbout_2)
        self.menuHelp.addAction(self.actionHow_to_2)
        self.menuAction.addAction(self.actionRun)
        self.actionRun.triggered.connect(self.run_and_store)
        self.menuAction.addAction(self.actionQuit)
        self.actionQuit.triggered.connect(self.exit_app)
        self.menuBar.addAction(self.menuAction.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "PLC - Password leak finder"))
        self.run.setText(_translate("MainWindow", "RUN"))
        self.quit.setText(_translate("MainWindow", "Quit"))
        self.how_to.setText(_translate("MainWindow", "How to use:"))
        self.nr_1.setText(_translate(
            "MainWindow", "1. Type or Copy/Paste your password in the blank area."))
        self.nr_2.setText(_translate("MainWindow", "2. Click \"RUN\""))
        self.nr_3.setText(_translate(
            "MainWindow", "3. Check the results... Did you passed it?"))
        # my code here
        self.result.setText(_translate("MainWindow", ""))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuAction.setTitle(_translate("MainWindow", "Action"))
        self.actionAbout_2.setText(_translate("MainWindow", "About"))
        self.actionHow_to_2.setText(_translate("MainWindow", "How to"))
        self.actionRun.setText(_translate("MainWindow", "Run (ctrl+r)"))
        self.actionRun.setToolTip(_translate("MainWindow", "Run"))
        self.actionRun.setStatusTip(
            _translate("MainWindow", "Run the checker"))
        self.actionRun.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionQuit.setText(_translate("MainWindow", "Quit (alt+q)"))
        self.actionQuit.setToolTip(_translate("MainWindow", "Quit"))
        self.actionQuit.setStatusTip(
            _translate("MainWindow", "Quit the program"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Alt+Q"))

    def exit_app(self):
        QApplication.quit()

    def run_and_store(self):
        stored = (self.password_input.text())
        result = mainy(stored)
        self.result.setText(result)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
