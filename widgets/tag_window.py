# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tag.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication


class Ui_Tag(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(183, 184)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tag_label = QtWidgets.QLabel(self.centralwidget)
        self.tag_label.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.tag_label.setObjectName("tag_label")
        self.gridLayout.addWidget(self.tag_label, 0, 0, 1, 1)
        self.tag_text_edit = QtWidgets.QTextEdit(self.centralwidget)
        self.tag_text_edit.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.tag_text_edit.setObjectName("tag_text_edit")
        self.gridLayout.addWidget(self.tag_text_edit, 1, 0, 1, 1)
        self.tag_button = QtWidgets.QPushButton(self.centralwidget)
        self.tag_button.setObjectName("tag_button")
        self.gridLayout.addWidget(self.tag_button, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 183, 21))
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
        self.tag_label.setText(_translate("MainWindow", "Insert tag name below:"))
        self.tag_button.setText(_translate("MainWindow", "Done!"))
