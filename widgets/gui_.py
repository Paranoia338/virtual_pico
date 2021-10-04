# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_without_qgraphicsview.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1201, 713)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.tabs.setObjectName("tabs")
        self.tab_one = QtWidgets.QWidget()
        self.tab_one.setObjectName("tab_one")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_one)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.save = QtWidgets.QPushButton(self.tab_one)
        self.save.setMinimumSize(QtCore.QSize(30, 30))
        self.save.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/buttons_icons/floppy-disk.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save.setIcon(icon)
        self.save.setIconSize(QtCore.QSize(30, 30))
        self.save.setFlat(False)
        self.save.setObjectName("save")
        self.horizontalLayout_2.addWidget(self.save)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(400, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.play_pause = QtWidgets.QPushButton(self.tab_one)
        self.play_pause.setMinimumSize(QtCore.QSize(30, 30))
        self.play_pause.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/buttons_icons/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play_pause.setIcon(icon1)
        self.play_pause.setIconSize(QtCore.QSize(30, 30))
        self.play_pause.setShortcut("")
        self.play_pause.setFlat(False)
        self.play_pause.setObjectName("play_pause")
        self.horizontalLayout_3.addWidget(self.play_pause)
        self.stop = QtWidgets.QPushButton(self.tab_one)
        self.stop.setMinimumSize(QtCore.QSize(30, 30))
        self.stop.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/buttons_icons/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stop.setIcon(icon2)
        self.stop.setIconSize(QtCore.QSize(30, 30))
        self.stop.setAutoDefault(False)
        self.stop.setDefault(False)
        self.stop.setFlat(False)
        self.stop.setObjectName("stop")
        self.horizontalLayout_3.addWidget(self.stop)
        self.recordingSlider = QtWidgets.QSlider(self.tab_one)
        self.recordingSlider.setMinimumSize(QtCore.QSize(150, 0))
        self.recordingSlider.setOrientation(QtCore.Qt.Horizontal)
        self.recordingSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.recordingSlider.setTickInterval(0)
        self.recordingSlider.setObjectName("recordingSlider")
        self.horizontalLayout_3.addWidget(self.recordingSlider)
        self.line_3 = QtWidgets.QFrame(self.tab_one)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_3.addWidget(self.line_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.time_label = QtWidgets.QLabel(self.tab_one)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.time_label.setFont(font)
        self.time_label.setObjectName("time_label")
        self.verticalLayout.addWidget(self.time_label)
        self.timeEdit = QtWidgets.QTimeEdit(self.tab_one)
        self.timeEdit.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhPreferNumbers|QtCore.Qt.ImhTime)
        self.timeEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.timeEdit.setCurrentSection(QtWidgets.QDateTimeEdit.HourSection)
        self.timeEdit.setObjectName("timeEdit")
        self.verticalLayout.addWidget(self.timeEdit)
        self.set_rec_time = QtWidgets.QPushButton(self.tab_one)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.set_rec_time.setFont(font)
        self.set_rec_time.setIconSize(QtCore.QSize(16, 16))
        self.set_rec_time.setFlat(False)
        self.set_rec_time.setObjectName("set_rec_time")
        self.verticalLayout.addWidget(self.set_rec_time)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.line = QtWidgets.QFrame(self.tab_one)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_3.addWidget(self.line)
        self.zoom_in = QtWidgets.QPushButton(self.tab_one)
        self.zoom_in.setMinimumSize(QtCore.QSize(30, 30))
        self.zoom_in.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/buttons_icons/zoom_in.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoom_in.setIcon(icon3)
        self.zoom_in.setIconSize(QtCore.QSize(30, 30))
        self.zoom_in.setFlat(False)
        self.zoom_in.setObjectName("zoom_in")
        self.horizontalLayout_3.addWidget(self.zoom_in)
        self.zoom_out = QtWidgets.QPushButton(self.tab_one)
        self.zoom_out.setMinimumSize(QtCore.QSize(30, 30))
        self.zoom_out.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/buttons_icons/zoom_out.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoom_out.setIcon(icon4)
        self.zoom_out.setIconSize(QtCore.QSize(30, 30))
        self.zoom_out.setFlat(False)
        self.zoom_out.setObjectName("zoom_out")
        self.horizontalLayout_3.addWidget(self.zoom_out)
        self.line_2 = QtWidgets.QFrame(self.tab_one)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_3.addWidget(self.line_2)
        spacerItem1 = QtWidgets.QSpacerItem(400, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.splitter_2 = QtWidgets.QSplitter(self.tab_one)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.list = QtWidgets.QTreeWidget(self.splitter)
        self.list.setObjectName("list")
        self.mini_timeline = QtWidgets.QGraphicsView(self.splitter_2)
        self.mini_timeline.setObjectName("mini_timeline")
        self.gridLayout_3.addWidget(self.splitter_2, 1, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 1, 1, 1)
        self.tabs.addTab(self.tab_one, "")
        self.gridLayout.addWidget(self.tabs, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1201, 21))
        self.menubar.setObjectName("menubar")
        self.menuNew = QtWidgets.QMenu(self.menubar)
        self.menuNew.setObjectName("menuNew")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_Project = QtWidgets.QAction(MainWindow)
        self.actionNew_Project.setObjectName("actionNew_Project")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionNew_Project_2 = QtWidgets.QAction(MainWindow)
        self.actionNew_Project_2.setObjectName("actionNew_Project_2")
        self.actionOpen_2 = QtWidgets.QAction(MainWindow)
        self.actionOpen_2.setObjectName("actionOpen_2")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionClose_project = QtWidgets.QAction(MainWindow)
        self.actionClose_project.setObjectName("actionClose_project")
        self.actionRename_Project = QtWidgets.QAction(MainWindow)
        self.actionRename_Project.setObjectName("actionRename_Project")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionNew_Project_3 = QtWidgets.QAction(MainWindow)
        self.actionNew_Project_3.setObjectName("actionNew_Project_3")
        self.menuNew.addAction(self.actionNew_Project_3)
        self.menuNew.addAction(self.actionOpen_2)
        self.menuNew.addAction(self.actionNew_Project_2)
        self.menuNew.addAction(self.actionSave_As)
        self.menuNew.addAction(self.actionRename_Project)
        self.menuNew.addAction(self.actionClose_project)
        self.menuNew.addAction(self.actionExit)
        self.menubar.addAction(self.menuNew.menuAction())

        self.retranslateUi(MainWindow)
        self.tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Lorenzo_Tool"))
        self.time_label.setText(_translate("MainWindow", "Insert recording time:"))
        self.timeEdit.setDisplayFormat(_translate("MainWindow", "hh:mm:ss:zzz"))
        self.set_rec_time.setText(_translate("MainWindow", "Set time!"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_one), _translate("MainWindow", "Timeline"))
        self.menuNew.setTitle(_translate("MainWindow", "File"))
        self.actionNew_Project.setText(_translate("MainWindow", "New Project"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionNew_Project_2.setText(_translate("MainWindow", "Save"))
        self.actionOpen_2.setText(_translate("MainWindow", "Open..."))
        self.actionSave_As.setText(_translate("MainWindow", "Save As..."))
        self.actionClose_project.setText(_translate("MainWindow", "Close"))
        self.actionRename_Project.setText(_translate("MainWindow", "Rename"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionNew_Project_3.setText(_translate("MainWindow", "New Project..."))

# import resources_rc
import resources.resources_rc
