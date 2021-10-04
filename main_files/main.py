import pprint
import sys
import threading
from functools import partial

from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSignal, Qt, QSize, QObject, QCoreApplication, QPointF, QTimer, QProcess
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QColor, QFont, QCursor
from PyQt5.QtWidgets import *

from Model.standard_item import StandardItem
from main_files.create_first_file import InitializeFile
from main_files.different_windows import AddItemsToList, Parameters
from styles.style import timeEdit_style
from widgets.gui_ import Ui_MainWindow
from widgets.range_slider import QRangeSlider
from widgets.time_editor_graphics_scene import MyGraphicsScene
from widgets.time_editor_graphics_view import MyGraphicsView

InitializeFile()


class MainWindow:
    resized = pyqtSignal()
    start_width = 1200
    start_height = 600

    # treeModel = QStandardItemModel()

    def __init__(self):
        # self.process = QProcess()  #This variable is used only for opening OS applications processes
        """ Different variables needed in a couple of functions in this class """
        self.scene_width = None
        self.scene_mouse_position_x = None
        self.scene_mouse_position_y = None
        self.length_of_recording_in_miliseconds = 1000
        self.position_zero_pad = None
        self.tree_root = None
        self.item_list = None
        # self.name = None
        self.new_stimuli_name = None
        self.new_stimuli_group = None

        self.global_keys = []
        self.global_values = []

        """ Create the current window in which we will attach the gui created in QT Creator """
        self.main_window = QMainWindow()
        """ Set the dimensions of the window """
        # self.main_window.resize(1201, 620)

        """ Set the value of the inferface created in QT Creator and converted in gui.py in the variable called "self.gui" """
        """ "Ui_Main_Window" is a class generated inside gui.py which contains the setup for the actual interface """
        self.gui = Ui_MainWindow()

        """ By calling the "setupUi" function we insert the variable "self.gui" in the newly created main window called "self.main_window" """
        self.gui.setupUi(
            self.main_window)

        """ Assigning resize event of main window to a function created by us """
        # self.main_window.resizeEvent = self.showCurrentSize_Window
        """ Assigning resize event of the timeline to a function created by us """
        # self.gui.timeline.resizeEvent = self.showCurrentSize_Timeline
        """ Assigning resize event of the slider to a function created by us """
        self.gui.mini_timeline.resizeEvent = self.showCurrentSize_MiniTimeline

        """ Set the dimensions limits of the main 3 widgets """
        self.gui.list.setMaximumWidth(400)
        self.gui.list.setMinimumWidth(151)
        self.gui.list.resize(151, 501)

        """Create graphics scene"""
        self.grScene = MyGraphicsScene()
        self.scene_width = self.grScene.width()
        # print(self.scene_width)
        self.position_zero_pad = self.grScene.pad_item.pos()

        self.timeline = MyGraphicsView(self.grScene, parent=self.gui.splitter)
        self.timeline.setObjectName("timeline")

        self.timeline.centerOn(-1200, -900)

        # """ Set the dimensions limits of the main 3 widgets """
        # self.timeline.setMaximumWidth(16777215)
        # self.timeline.setMinimumWidth(300)
        # self.timeline.resize(1024, 501)

        """ Setting the maximum stretch of the slider widget """
        # self.gui.mini_timeline.setMaximumWidth(16777215)
        self.gui.mini_timeline.setMaximumHeight(60)

        """ Here we are going to add the slider from internet to the location inside mini_timeline """
        self.slider = QRangeSlider(self.gui.mini_timeline)

        # trying something
        self.slider_start_position = None
        self.slider_end_position = None
        self.slider.startValueChanged.connect(self.get_slider_x)
        self.slider.endValueChanged.connect(self.get_slider_y)

        # trying something new
        self.mini_width = None
        self.time_line_width = None
        # self.scene_view_ratio = None

        # Implementing the context menu from the treeview widget
        # self.gui.list.clicked.connect(self.getItemIndex)
        self.gui.list.contextMenuEvent = self.create_list_context_menu

        self.gui.zoom_in.clicked.connect(self.timeline.zoom_in)
        self.gui.zoom_out.clicked.connect(self.timeline.zoom_out)
        # self.gui.save.clicked.connect(self.read_group_name)
        self.gui.list.clicked.connect(self.read_group_name)

        self.list_menu = QMenu()
        self.create_group = QAction("Add group")
        self.create_stimuli = QAction("Add stimuli")
        self.show_parameters = QAction("Parameters")
        self.remove_group = QAction("Remove group")
        self.remove_stimuli = QAction("Remove stimuli")

        self.create_group.triggered.connect(self.addGroupToList)
        self.create_stimuli.triggered.connect(self.addSimulation)
        self.show_parameters.triggered.connect(self.parameters_window)
        self.remove_group.triggered.connect(self.delete_group)
        self.remove_stimuli.triggered.connect(self.delete_stimuli)

        self.list_menu.addActions([self.create_group, self.create_stimuli, self.remove_group, self.remove_stimuli, self.show_parameters])

        """ Here is created the treeview at runtime """
        self.createTreeView()

        """ Getting the time changed event from the QTimeEdit widget """
        self.gui.timeEdit.timeChanged.connect(self.get_time)
        # self.gui.set_rec_time.clicked.connect(self.get_time)

        """ An attempt to change the height and width of the plus and minus buttons of QTimeEdit widget """
        self.gui.timeEdit.setStyleSheet(timeEdit_style)

        """ Here the animation is triggered """
        self.icon2_pause = QtGui.QIcon()
        self.icon2_pause.addPixmap(QtGui.QPixmap(":/buttons_icons/pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.icon2_play = QtGui.QIcon()
        self.icon2_play.addPixmap(QtGui.QPixmap(":/buttons_icons/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.gui.play_pause.clicked.connect(self.start_pad_animation)
        self.gui.stop.clicked.connect(self.reset_pad_position)

    """
    The function which will run when the "resize event" of the main window (self.main_window) takes place and emits a signal to this function ( the "event" argument is the signal )
    The "resize event" is defined by us in the line 56. Based on the values of the width and height we will resize the elements inside the GraphicsView widget and also the widget itself.
    """

    # def showCurrentSize_Window(self, event):
    #     global mainWindow_width
    #     global mainWindow_heigth
    #     mainWindow_width = self.main_window.width()
    #     mainWindow_heigth = self.main_window.height()
    #     print("Latime MainWindow: ", mainWindow_width, "Inaltime MainWindow: ", mainWindow_heigth)

    def showCurrentSize_Timeline(self, event):
        global timeline_width
        global timeline_heigth
        timeline_width = self.timeline.width()
        timeline_heigth = self.timeline.height()
        self.grScene.setSceneRect(0, 0, timeline_width, timeline_heigth)

    def showCurrentSize_MiniTimeline(self, event):
        global mini_timeline_width
        global mini_timeline_heigth
        mini_timeline_width = self.gui.mini_timeline.width()
        self.mini_width = mini_timeline_width
        # print(mini_timeline_width)
        mini_timeline_heigth = self.gui.mini_timeline.height()
        self.slider.setFixedHeight(mini_timeline_heigth)
        self.slider.setFixedWidth(mini_timeline_width)

    def getItemIndex(self, val):
        # pass
        print(val.row())
        print(val.data())

        # self.currentTreeIndex = val.row()
        # self.global_val = val
        # self.currentTreeData = val.data()
        # print(self.currentTreeIndex)

    # Add new group names or simulations from treeview context menu and process the actions
    def addGroupToList(self):
        self.name_group_window = AddItemsToList('group')
        self.name_group_window.signal_tree_view.tip_signal_gr.connect(self.create_new_group)
        self.name_group_window.show()

    def addSimulation(self):
        self.name_simu_window = AddItemsToList('simulation')
        self.name_simu_window.signal_tree_view.tip_signal_sim.connect(self.create_new_simulation)
        self.name_simu_window.show()

    def parameters_window(self):
        # self.para_window = Parameters(self.currentTreeData)
        self.para_window = Parameters()
        self.para_window.show()

    def create_new_group(self, text):
        new_group_data = {text: []}
        self.item_list.append(new_group_data)
        new_group = QTreeWidgetItem(self.gui.list)
        new_group.setText(0, text)
        # pprint.pprint(self.item_list)
        # self.gui.list.update()
        self.new_stimuli_group = text

        #  This version works only if we have the self.tree_root parent

        # new_group_data = {text: []}
        # self.item_list.append(new_group_data)
        # new_group = QTreeWidgetItem()
        # new_group.setText(0, text)
        # self.tree_root.addChild(new_group)
        # # pprint.pprint(self.item_list)
        # # self.gui.list.update()
        # self.new_stimuli_group = text

    def delete_group(self):
        # pass
        if self.new_stimuli_name in self.global_keys:
            print("Ai selectat un grup")
        else:
            print("Ai selectat un stimul")

        # the_object = self.gui.list.selectedItems()[0]
        # print(the_object.data)
        # parent_of_group = the_object.parent()
        # self.gui.list.removeChild()

        # the_object = self.gui.list.selectedItems()[0]
        # parent_of_group = the_object.parent()
        # self.tree_root.removeChild(parent_of_group)
        # # self.gui.list.update()

    def create_new_simulation(self, text):
        # pass
        the_object = self.gui.list.selectedItems()[0]
        new_stimuli = QTreeWidgetItem()
        new_stimuli.setText(0, text)
        the_object.addChild(new_stimuli)

        dict_index = self.get_dict_index()
        self.item_list[dict_index][self.new_stimuli_group].append(text)

        # object_parent = the_object.parent()
        # print(object_parent.data())

    def get_dict_index(self):
        dict_index = None
        for index, dictionary_item in enumerate(self.item_list):
            the_stimuli_dict = dictionary_item.get(self.new_stimuli_name)
            if the_stimuli_dict is not None:
                dict_index = index
        print(dict_index)
        return dict_index


    def delete_stimuli(self):
        the_object = self.gui.list.selectedItems()[0]
        parent_of_object = the_object.parent()
        parent_of_object.removeChild(the_object)
        # self.gui.list.update()

    def create_list_context_menu(self, event):
        self.list_menu.exec_(QCursor.pos())

    def read_group_name(self, val):
        self.new_stimuli_name = val.data()
        self.get_dict_index()
        # print(self.item_list)

        # for dictionary_item in self.item_list:
        #     list_of_stimuli = dictionary_item.get(self.new_stimuli_name)
        #     print(list_of_stimuli)

        # This variant was abandoned because of it's recurrence
        # print(name)
        # thread_search_stimuli = threading.Thread(target=self.thread_processing, args=(name, self.item_list))
        # thread_search_stimuli.start()
        # thread_search_stimuli.join()


    # def thread_processing(self, stimuli_name, list_data):
    #     for dictionary_item in list_data:
    #         # list_of_stimuli = list(dictionary_item.keys())
    #         # print(list_of_stimuli)
    #         list_of_stimuli = dictionary_item.get(stimuli_name)
    #         print(list_of_stimuli)


    # def createTreeView(self):
    #     self.gui.list.setIndentation(0)
    #     self.gui.list.setAlternatingRowColors(True)
    #     self.gui.list.setHeaderHidden(True)
    #     self.rootNode = self.treeModel.invisibleRootItem()
    #
    #     # commands_names = [("Ionut", "Andrei", "Irinel", "Gabriela"), "Vasile", ("Ion",  "Gheorghe")]
    #     commands_names = ["Gabriela", "Ionut", "Andrei", "Irinel", "Vasile", "Ion", "Gheorghe"]
    #     currents = []
    #     # categories = []
    #     for x in commands_names:
    #         item = StandardItem(x, 12, color=QColor(0, 0, 0))
    #         currents.append(item)
    #     self.rootNode.appendRows(currents)
    #     self.gui.list.setModel(self.treeModel)
    #     self.gui.list.setCurrentIndex(self.treeModel.index(0, 0))

    def createTreeView(self):
        # pass
        self.gui.list.setColumnCount(0)
        self.gui.list.setHeaderLabel("Groups of stimuli")
        # self.gui.list.setHeaderHidden(True)
        # self.gui.list.setIndentation(0)

        # self.tree_root = QTreeWidgetItem(self.gui.list)
        # self.tree_root.setText(0, 'Datafile name')
        # self.tree_root.setExpanded(True)
        # self.gui.list.addTopLevelItem(self.tree_root)

        # # commands_names = [("Ionut", "Andrei", "Irinel", "Gabriela"), "Vasile", ("Ion",  "Gheorghe")]
        # commands_names = ["Gabriela", "Ionut", "Andrei", "Irinel", "Vasile", "Ion", "Gheorghe"]
        # for x in commands_names:
        #     child_item = QTreeWidgetItem()
        #     child_item.setText(0, x)
        #     tree_root.addChild(child_item)

        self.item_list = [{"First Group": ["Stimuli 1", "Stimuli 2"]}, {"Second Group": ["Stimuli 1", "Stimuli 2"]}]
        # keys = []
        # values = []
        # self.global_keys
        # self.global_values

        for x in self.item_list:
            key = list(x.keys())
            self.global_keys.append(key[0])
            value = list(x.values())
            # print(value)
            self.global_values.append(value[0])

        # print(keys)
        # print(values)

        for y in range(0, len(self.global_keys)):
            # item = QTreeWidgetItem()
            item = QTreeWidgetItem(self.gui.list)
            text = self.global_keys[y]
            item.setText(0, text)
            font = QFont('Open Sans', 10)
            # font.setBold(False)
            item.setFont(0, font)
            child_items = self.global_values[y]
            for z in child_items:
                font_size = 10
                set_bold = False
                # color = QColor(0, 0, 0)
                font = QFont('Open Sans', font_size)
                # font.setBold(set_bold)
                child_item = QTreeWidgetItem()
                child_item.setFont(0, font)
                # child_item.setSizeHint(0, QSize(40, 40))
                child_item.setText(0, z)
                item.addChild(child_item)
            # self.tree_root.addChild(item)


        # for x in self.item_list:
        #     key = list(x.keys())
        #     keys.append(key[0])
        #     value = list(x.values())
        #     # print(value)
        #     values.append(value[0])
        #
        # # print(keys)
        # # print(values)
        #
        # for y in range(0, len(keys)):
        #     # item = QTreeWidgetItem()
        #     item = QTreeWidgetItem(self.gui.list)
        #     text = keys[y]
        #     item.setText(0, text)
        #     font = QFont('Open Sans', 10)
        #     # font.setBold(False)
        #     item.setFont(0, font)
        #     child_items = values[y]
        #     for z in child_items:
        #         font_size = 10
        #         set_bold = False
        #         # color = QColor(0, 0, 0)
        #         font = QFont('Open Sans', font_size)
        #         # font.setBold(set_bold)
        #         child_item = QTreeWidgetItem()
        #         child_item.setFont(0, font)
        #         # child_item.setSizeHint(0, QSize(40, 40))
        #         child_item.setText(0, z)
        #         item.addChild(child_item)
        #     # self.tree_root.addChild(item)



    """ Calling the function which makes the main window to appear on screen """

    def show(self):
        self.main_window.show()

    def get_slider_x(self, x):
        self.slider_start_position = x
        # print(x)

    def get_slider_y(self, y):
        self.slider_start_position = y
        # print(y)

    def timeline_position_change(self, pos):
        pass
        # middle = self.slider.width()//2
        # if self.slider_start_position < middle:
        #     pass
        # else:
        #     new_x_loc = -1200 - (self.slider_start_position - middle)
        #     self.grScene.setSceneRect(self.grScene.sceneRect().translated(new_x_loc, 0))
        #     self.timeline.centerOn(new_x_loc, -900)


    def get_time(self):
        time = self.gui.timeEdit.time().toPyTime()
        print(type(self.gui.timeEdit.time()))
        hours = time.hour
        """ 1 Hour is 3.600.000 Miliseconds so in order to get only miliseconds we should multiply hours with 3.600.000"""
        hours_2_miliseconds = hours * 3600000
        # print(hours_2_miliseconds)
        minutes = time.minute
        """ 1 Minute has 60.000 Miliseconds so in order to get only miliseconds we should multiply the minutes with 60.000 """
        minutes_2_miliseconds = minutes * 60000
        # print(minutes_2_miliseconds)
        seconds = time.second
        """ 1 second has 1000 miliseconds so in order to have only miliseconds we should multiply the seconds with 1000 """
        seconds_2_miliseconds = seconds * 1000
        # print(seconds_2_miliseconds)
        microseconds = time.microsecond
        """ 1000 Microsecond = 1 Milisecond so in order to get the miliseconds, we should divide the microseconds to 1000"""
        microseconds_2_miliseconds = microseconds // 1000
        # print(microseconds_2_miliseconds)
        total_miliseconds = hours_2_miliseconds + minutes_2_miliseconds + seconds_2_miliseconds + microseconds_2_miliseconds
        # print(f"There are {total_miliseconds} miliseconds in the recording")
        self.length_of_recording_in_miliseconds = total_miliseconds
        # self.slider.setMax(self.length_of_recording_in_miliseconds)
        # self.slider.update()

    # def calculate_ratio_scene_view(self):
        # scene_view_ratio = self.time_line_width/2400

    def start_pad_animation(self):
        self.gui.play_pause.setIcon(self.icon2_pause)
        self.gui.play_pause.setIconSize(QSize(30, 30))
        self.gui.play_pause.update()

        self.grScene.pad_item.move(duration=self.length_of_recording_in_miliseconds, pixels=1000)

        self.gui.play_pause.setIcon(self.icon2_play)
        self.gui.play_pause.setIconSize(QSize(30, 30))


    def reset_pad_position(self):
        self.grScene.pad_item.setPos(self.position_zero_pad)


if __name__ == "__main__":
    app_context = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app_context.exec_())
