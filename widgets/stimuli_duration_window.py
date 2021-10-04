# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'set_duration.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StimuliDuration(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(447, 230)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.duration_edit = QtWidgets.QTimeEdit(self.centralwidget)
        self.duration_edit.setMinimumSize(QtCore.QSize(0, 160))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.duration_edit.setFont(font)
        self.duration_edit.setStyleSheet("font: 36pt \"MS Shell Dlg 2\";")
        self.duration_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.duration_edit.setCurrentSection(QtWidgets.QDateTimeEdit.HourSection)
        self.duration_edit.setCurrentSectionIndex(0)
        self.duration_edit.setObjectName("duration_edit")
        self.verticalLayout.addWidget(self.duration_edit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.duration_button = QtWidgets.QPushButton(self.centralwidget)
        self.duration_button.setMinimumSize(QtCore.QSize(170, 40))
        self.duration_button.setObjectName("duration_button")
        self.horizontalLayout.addWidget(self.duration_button)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Set the duration of stimuli"))
        self.duration_edit.setDisplayFormat(_translate("MainWindow", "hh:mm:ss:zzz"))
        self.duration_button.setText(_translate("MainWindow", "Done !"))
