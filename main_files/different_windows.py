from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QMainWindow, QShortcut

from main_files.custom_signals import TreeViewCustomSignal, Signals
from styles.style import stimuli_duration_style
# from tree_view_samples.model_view_test.model_index import MainForm
from widgets.parameters import Ui_Parameters
from widgets.stimuli_duration_window import Ui_StimuliDuration
from widgets.stimuli_parameters import Ui_Stimuli_Params
from widgets.tag_window import Ui_Tag


class DurationWindow:
    # signal_duration = Signals()
    def __init__(self):
        self.signal_duration = Signals()
        self.duration_window = QMainWindow()
        self.gui = Ui_StimuliDuration()
        self.gui.setupUi(
            self.duration_window)
        # self.duration_window.setFixedWidth(500)
        self.duration_window.setWindowTitle("Set stimuli duration in milliseconds")
        self.gui.duration_edit.setStyleSheet(stimuli_duration_style)
        self.gui.duration_button.clicked.connect(self.done)

    def done(self):
        duration_time = self.gui.duration_edit.time()
        self.signal_duration.stimuli_duration_signal.emit(duration_time)
        self.duration_window.close()

    def show(self):
        self.duration_window.show()


class TagWindow:
    # signal_tag = Signals()
    def __init__(self):
        self.signal_tag = Signals()
        self.tag_window = QMainWindow()
        self.gui = Ui_Tag()
        self.gui.setupUi(
            self.tag_window)
        self.tag_window.setFixedWidth(500)
        self.tag_window.setWindowTitle("Tag your stimuli")
        self.gui.tag_button.clicked.connect(self.done)

    def done(self):
        tag_text = self.gui.tag_text_edit.toPlainText()
        self.signal_tag.tag_name.emit(tag_text)
        self.tag_window.close()

    def show(self):
        self.tag_window.show()


class StimuliParameters:
    # def __init__(self, stimuli_name):
    #     self.stimuli_name = stimuli_name
    def __init__(self):
        self.stimuli_params_window = QMainWindow()
        self.gui = Ui_Stimuli_Params()
        self.gui.setupUi(
            self.stimuli_params_window)
        self.stimuli_params_window.setFixedWidth(1000)
        self.stimuli_params_window.setWindowTitle("Parameters")

    def show(self):
        self.stimuli_params_window.show()


class Parameters:
    # def __init__(self, stimuli_name):
    #     self.stimuli_name = stimuli_name
    def __init__(self):
        self.parameters_window = QMainWindow()
        self.gui = Ui_Parameters()
        self.gui.setupUi(
            self.parameters_window)

        # self.tip_window.setFixedWidth(500)
        self.parameters_window.setWindowTitle("Parameters")

    def show(self):
        self.parameters_window.show()


class AddItemsToList:
    # signal_tree_view = TreeViewCustomSignal()
    def __init__(self, tip):
        # self.shortcut_close = QShortcut(QKeySequence(Qt.CTRL + Qt.Key_Return), self)
        # self.shortcut_close.activated.connect(self.done)
        self.signal_tree_view = TreeViewCustomSignal()
        self.tip = tip
        self.tip_window = QMainWindow()
        self.gui = Ui_Tag()
        self.gui.setupUi(
            self.tip_window)

        self.tip_window.setFixedWidth(500)

        if self.tip == "group":
            self.tip_window.setWindowTitle("Add a group to the list")
            self.gui.tag_label.setText("Insert the name of the new group")

        elif self.tip == "simulation":
            self.tip_window.setWindowTitle("Add a simulation to the group")
            self.gui.tag_label.setText("Insert the name of the new simulation")

        self.gui.tag_button.clicked.connect(self.done)

    # The below function does not work because when we press 'Enter' the application is focused on the text edit widget and the enter action is performed as an new line command instead of triggering the self.done() function
    # def keyPressEvent(self, event):
    #     if event.key() == Qt.Key_Return:
    #         self.done()

    def done(self):
        tip_text = self.gui.tag_text_edit.toPlainText()
        if self.tip == "group":
            self.signal_tree_view.tip_signal_gr.emit(tip_text)
            # self.signal_tree_view.tip_signal_gr.connect(MainForm.create_new_group)
        elif self.tip == "simulation":
            self.signal_tree_view.tip_signal_sim.emit(tip_text)
            # self.signal_tree_view.tip_signal_gr.connect(MainForm.create_new_simulation)
        self.tip_window.close()

    def show(self):
        self.tip_window.show()
